"""
SSE клиент для тестирования FastMCP сервера.
Реализует асинхронное подключение через Server-Sent Events.
"""

import logging
from contextlib import asynccontextmanager
from typing import Any
from urllib.parse import urljoin, urlparse

import anyio
import httpx
from anyio.abc import TaskStatus
from anyio.streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream
from httpx_sse import aconnect_sse

import mcp.types as types
from mcp.shared._httpx_utils import McpHttpClientFactory, create_mcp_http_client
from mcp.shared.message import SessionMessage

logger = logging.getLogger(__name__)

def remove_request_params(url: str) -> str:
    """Удаляет параметры запроса из URL."""
    return urljoin(url, urlparse(url).path)

@asynccontextmanager
async def sse_client(
    url: str,
    headers: dict[str, Any] | None = None,
    timeout: float = 5,
    sse_read_timeout: float = 60 * 5,
    httpx_client_factory: McpHttpClientFactory = create_mcp_http_client,
    auth: httpx.Auth | None = None,
):
    """
    Клиентский транспорт для SSE.
    
    Args:
        url: URL SSE эндпоинта
        headers: Опциональные HTTP заголовки
        timeout: Таймаут для HTTP операций
        sse_read_timeout: Таймаут для чтения SSE событий
        httpx_client_factory: Фабрика для создания HTTP клиента
        auth: Опциональная HTTP аутентификация
    """
    read_stream: MemoryObjectReceiveStream[SessionMessage | Exception]
    read_stream_writer: MemoryObjectSendStream[SessionMessage | Exception]
    write_stream: MemoryObjectSendStream[SessionMessage]
    write_stream_reader: MemoryObjectReceiveStream[SessionMessage]

    read_stream_writer, read_stream = anyio.create_memory_object_stream(0)
    write_stream, write_stream_reader = anyio.create_memory_object_stream(0)

    async with anyio.create_task_group() as tg:
        try:
            logger.info(f"Подключение к SSE эндпоинту: {remove_request_params(url)}")
            async with httpx_client_factory(headers=headers, auth=auth) as client:
                async with aconnect_sse(
                    client,
                    "GET",
                    url,
                    timeout=httpx.Timeout(timeout, read=sse_read_timeout),
                ) as event_source:
                    event_source.response.raise_for_status()
                    logger.debug("SSE соединение установлено")

                    async def sse_reader(
                        task_status: TaskStatus[str] = anyio.TASK_STATUS_IGNORED,
                    ):
                        try:
                            async for sse in event_source.aiter_sse():
                                logger.debug(f"Получено SSE событие: {sse.event}")
                                match sse.event:
                                    case "endpoint":
                                        endpoint_url = urljoin(url, sse.data)
                                        logger.info(f"Получен URL эндпоинта: {endpoint_url}")

                                        url_parsed = urlparse(url)
                                        endpoint_parsed = urlparse(endpoint_url)
                                        if (
                                            url_parsed.netloc != endpoint_parsed.netloc
                                            or url_parsed.scheme != endpoint_parsed.scheme
                                        ):
                                            error_msg = (
                                                "Происхождение эндпоинта не совпадает с "
                                                f"происхождением соединения: {endpoint_url}"
                                            )
                                            logger.error(error_msg)
                                            raise ValueError(error_msg)

                                        task_status.started(endpoint_url)

                                    case "message":
                                        try:
                                            message = types.JSONRPCMessage.model_validate_json(sse.data)
                                            logger.debug(f"Получено сообщение сервера: {message}")
                                        except Exception as exc:
                                            logger.error(f"Ошибка парсинга сообщения сервера: {exc}")
                                            await read_stream_writer.send(exc)
                                            continue

                                        session_message = SessionMessage(message)
                                        await read_stream_writer.send(session_message)
                                    case _:
                                        logger.warning(f"Неизвестное SSE событие: {sse.event}")
                        except Exception as exc:
                            logger.error(f"Ошибка в sse_reader: {exc}")
                            await read_stream_writer.send(exc)
                        finally:
                            await read_stream_writer.aclose()

                    async def post_writer(endpoint_url: str):
                        try:
                            async with write_stream_reader:
                                async for session_message in write_stream_reader:
                                    logger.debug(f"Отправка сообщения клиента: {session_message}")
                                    response = await client.post(
                                        endpoint_url,
                                        json=session_message.message.model_dump(
                                            by_alias=True,
                                            mode="json",
                                            exclude_none=True,
                                        ),
                                    )
                                    response.raise_for_status()
                                    logger.debug(
                                        "Сообщение клиента успешно отправлено: "
                                        f"{response.status_code}"
                                    )
                        except Exception as exc:
                            logger.error(f"Ошибка в post_writer: {exc}")
                        finally:
                            await write_stream.aclose()

                    endpoint_url = await tg.start(sse_reader)
                    logger.info(f"Запуск post_writer с URL эндпоинта: {endpoint_url}")
                    tg.start_soon(post_writer, endpoint_url)

                    try:
                        yield read_stream, write_stream
                    finally:
                        tg.cancel_scope.cancel()
        finally:
            await read_stream_writer.aclose()
            await write_stream.aclose() 