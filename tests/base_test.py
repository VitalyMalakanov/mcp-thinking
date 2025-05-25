"""
Базовый класс для тестов FastMCP сервера.
Содержит общую логику для всех тестов.
"""

import asyncio
import json
import logging
from typing import Any, Dict, Optional

from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
import enhanced_sequential_thinking_server as es

logger = logging.getLogger(__name__)

class BaseThinkingTest:
    """Базовый класс для тестов сервера мышления."""
    
    def setup_method(self):
        self.server_url = "http://localhost:8000/sse"
        self.thought_id: Optional[str] = None

    async def send_request(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Отправляет запрос к серверу через SSE и возвращает ответ.
        """
        async with sse_client(self.server_url) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                # Отправляем параметры как {'input': params}
                result = await session.call_tool(method, {"input": params})
                # Логируем сырое содержимое ответа
                logger.info(f"Raw result.content: {result.content}")
                if not result.content or not getattr(result.content[0], 'text', None):
                    raise RuntimeError(f"Пустой или некорректный ответ от сервера для метода {method}: {result.content}")
                return json.loads(result.content[0].text)

    async def create_thought(self, thought: str, thought_type: es.ThoughtType = es.ThoughtType.ANALYSIS,
                           strategy: es.ThinkingStrategy = es.ThinkingStrategy.CRITICAL,
                           tags: list[str] = None) -> Dict[str, Any]:
        """
        Создает новую мысль.
        
        Args:
            thought: Текст мысли
            thought_type: Тип мысли
            strategy: Стратегия мышления
            tags: Теги
            
        Returns:
            Dict[str, Any]: Результат создания мысли
        """
        input_data = es.EnhancedThinkingInput(
            thought=thought,
            thought_type=thought_type,
            strategy=strategy,
            tags=tags or [],
            request_analysis=True,
            request_validation=True
        )
        
        result = await self.send_request("enhanced_thinking", input_data.model_dump())
        if "thought_id" in result:
            self.thought_id = result["thought_id"]
        return result
    
    async def analyze_session(self) -> Dict[str, Any]:
        """
        Анализирует текущую сессию мышления.
        
        Returns:
            Dict[str, Any]: Результат анализа
        """
        return await self.send_request("analyze_thinking_session", {})
    
    async def metacognitive_reflection(self, focus_area: str, analysis_depth: int = 3) -> Dict[str, Any]:
        """
        Выполняет метапознавательное размышление.
        
        Args:
            focus_area: Область фокусировки
            analysis_depth: Глубина анализа
            
        Returns:
            Dict[str, Any]: Результат размышления
        """
        input_data = es.MetacognitionInput(
            focus_area=focus_area,
            analysis_depth=analysis_depth
        )
        return await self.send_request("metacognitive_reflection", input_data.model_dump())
    
    async def adapt_strategy(self, current_strategy: es.ThinkingStrategy,
                           effectiveness_score: float, context: str,
                           constraints: list[str] = None) -> Dict[str, Any]:
        """
        Адаптирует стратегию мышления.
        
        Args:
            current_strategy: Текущая стратегия
            effectiveness_score: Оценка эффективности
            context: Контекст
            constraints: Ограничения
            
        Returns:
            Dict[str, Any]: Результат адаптации
        """
        input_data = es.StrategyAdaptationInput(
            current_strategy=current_strategy,
            effectiveness_score=effectiveness_score,
            context=context,
            constraints=constraints or []
        )
        return await self.send_request("adapt_thinking_strategy", input_data.model_dump())
    
    async def get_thinking_path(self, thought_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Получает путь мышления для указанной мысли.
        
        Args:
            thought_id: ID мысли (если None, используется последняя созданная мысль)
            
        Returns:
            Dict[str, Any]: Путь мышления
        """
        thought_id = thought_id or self.thought_id
        if not thought_id:
            raise ValueError("Не указан ID мысли")
        return await self.send_request("get_thinking_path", {"thought_id": thought_id})
    
    async def export_session(self, format_type: str = "summary") -> Dict[str, Any]:
        """
        Экспортирует текущую сессию мышления.
        
        Args:
            format_type: Тип формата экспорта
            
        Returns:
            Dict[str, Any]: Результат экспорта
        """
        return await self.send_request("export_thinking_session", {"format_type": format_type})
    
    async def list_tools(self) -> list[str]:
        """
        Получает список доступных инструментов с сервера.
        Returns:
            list[str]: Список имён инструментов
        """
        async with sse_client(self.server_url) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                result = await session.list_tools()
                if hasattr(result, "tools") and result.tools:
                    return [tool.name for tool in result.tools]
                return [] 