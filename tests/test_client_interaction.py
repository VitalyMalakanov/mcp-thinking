import pytest
import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from pydantic import ValidationError, BaseModel
import pytest_asyncio

from enhanced_sequential_thinking_server import (
    EnhancedThinkingInput,
    MetacognitionInput,
    StrategyAdaptationInput,
    ThoughtType,
    ThinkingStrategy,
    ConfidenceLevel
)

# Убедитесь, что pytest.ini настроен:
# [pytest]
# asyncio_mode = strict
# asyncio_default_fixture_loop_scope = module

@pytest_asyncio.fixture(scope="module")
async def server_url():
    print("\n--- Ожидаем, что Enhanced MCP сервер запущен на http://localhost:8000 ---")
    yield "http://localhost:8000"
    print("\n--- Тестирование клиента завершено ---")

@pytest_asyncio.fixture(scope="module")
async def mcp_client_session(server_url):
    print(f"\n[Fixture] Попытка установить клиентскую сессию MCP к {server_url}/sse...")
    session = None
    try:
        async with sse_client(url=f"{server_url}/sse", timeout=20) as (read_stream, write_stream):
            print("[Fixture] Потоки SSE установлены. Создание ClientSession...")
            session = ClientSession(read_stream, write_stream)
            print("[Fixture] ClientSession создана. Инициализация сессии...")
            await session.initialize()
            print("[Fixture] Сессия успешно инициализирована.")
            yield session
    except asyncio.TimeoutError:
        print(f"[Fixture ERROR] Таймаут (20s) при установлении SSE соединения с {server_url}/sse.")
        pytest.fail(f"SSE connection to {server_url}/sse timed out.")
    except Exception as e:
        print(f"\n[Fixture ERROR] Не удалось установить клиентскую сессию MCP: {e}")
        pytest.fail(f"Could not establish MCP client session: {e}. Ensure server is running on {server_url}/sse")
    finally:
        if session:
            try:
                await session.close()
                print("[Fixture] Клиентская сессия MCP закрыта.")
            except Exception as e:
                print(f"[Fixture WARNING] Ошибка при закрытии сессии: {e}")

def pydantic_model_to_dict(model_instance: BaseModel):
    if hasattr(model_instance, 'model_dump'): 
        return model_instance.model_dump(exclude_none=True, by_alias=False) 
    elif hasattr(model_instance, 'dict'): 
        return model_instance.dict(exclude_none=True, by_alias=False)
    if isinstance(model_instance, dict):
        return model_instance
    return model_instance


@pytest.mark.asyncio(loop_scope="module") 
async def test_01_enhanced_thinking_basic(mcp_client_session):
    print("\n[Client Test] Тестируем создание мысли...")
    input_data_model = EnhancedThinkingInput(
        thought="Искусственный интеллект может значительно улучшить процесс принятия решений, но требует тщательного контроля и этических рамок.",
        thought_type=ThoughtType.ANALYSIS,
        strategy=ThinkingStrategy.CRITICAL,
        tags=["AI", "этика", "принятие решений"]
    )
    
    try:
        # FIX: Увеличиваем таймаут, особенно для первого вызова
        result = await asyncio.wait_for(
            mcp_client_session.call_tool("enhanced_thinking", pydantic_model_to_dict(input_data_model)),
            timeout=30 
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента enhanced_thinking превысил таймаут (30s)")

    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    
    result_data = json.loads(result[0].text)
    print(f"  Результат: {result_data}")
    
    assert "thought_id" in result_data
    assert "analysis" in result_data
    pytest.global_thought_id = result_data["thought_id"]

@pytest.mark.asyncio(loop_scope="module") 
async def test_02_analyze_thinking_session(mcp_client_session):
    print("\n[Client Test] Тестируем анализ сессии...")
    if not hasattr(pytest, 'global_thought_id'):
        await test_01_enhanced_thinking_basic(mcp_client_session)
    
    try:
        analysis_result = await asyncio.wait_for(
            mcp_client_session.call_tool("analyze_thinking_session"), 
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента analyze_thinking_session превысил таймаут (20s)")
        
    assert analysis_result is not None
    analysis_data = json.loads(analysis_result[0].text)
    print(f"  Анализ сессии: {analysis_data}")
    assert "coherence_score" in analysis_data
    assert analysis_data["thought_count"] > 0

@pytest.mark.asyncio(loop_scope="module") 
async def test_03_metacognitive_reflection(mcp_client_session):
    print("\n[Client Test] Тестируем метапознавательное размышление...")
    meta_input_model = MetacognitionInput(
        focus_area="Эффективность критического мышления",
        analysis_depth=3
    )
    try:
        meta_result = await asyncio.wait_for(
            mcp_client_session.call_tool("metacognitive_reflection", pydantic_model_to_dict(meta_input_model)),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента metacognitive_reflection превысил таймаут (20s)")
        
    assert meta_result is not None
    meta_data = json.loads(meta_result[0].text)
    print(f"  Метапознавательный анализ: {meta_data}")
    assert "focus_area" in meta_data
    assert "thinking_patterns" in meta_data

@pytest.mark.asyncio(loop_scope="module") 
async def test_04_adapt_thinking_strategy(mcp_client_session):
    print("\n[Client Test] Тестируем адаптацию стратегии...")
    strategy_input_model = StrategyAdaptationInput(
        current_strategy=ThinkingStrategy.CRITICAL,
        effectiveness_score=0.7,
        context="Анализ этических аспектов ИИ",
        constraints=["время", "ресурсы"]
    )
    try:
        strategy_result = await asyncio.wait_for(
            mcp_client_session.call_tool("adapt_thinking_strategy", pydantic_model_to_dict(strategy_input_model)),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента adapt_thinking_strategy превысил таймаут (20s)")

    assert strategy_result is not None
    strategy_data = json.loads(strategy_result[0].text)
    print(f"  Адаптация стратегии: {strategy_data}")
    assert "suggested_strategies" in strategy_data
    assert len(strategy_data["suggested_strategies"]) > 0

@pytest.mark.asyncio(loop_scope="module") 
async def test_05_get_thinking_path(mcp_client_session):
    print("\n[Client Test] Тестируем получение пути мышления...")
    if not hasattr(pytest, 'global_thought_id'):
        await test_01_enhanced_thinking_basic(mcp_client_session)
        
    thought_id_str = pytest.global_thought_id
    
    try:
        path_result = await asyncio.wait_for(
            mcp_client_session.call_tool("get_thinking_path", {"thought_id": thought_id_str}),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента get_thinking_path превысил таймаут (20s)")
        
    assert path_result is not None
    path_data = json.loads(path_result[0].text)
    print(f"  Путь мышления: {path_data}")
    assert "path" in path_data
    assert len(path_data["path"]) > 0
    assert path_data["path"][-1]["thought_id"] == thought_id_str

@pytest.mark.asyncio(loop_scope="module") 
async def test_06_export_thinking_session(mcp_client_session):
    print("\n[Client Test] Тестируем экспорт сессии (summary)...")
    try:
        export_summary_result = await asyncio.wait_for(
            mcp_client_session.call_tool("export_thinking_session", {"format_type": "summary"}),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента export_thinking_session (summary) превысил таймаут (20s)")
        
    assert export_summary_result is not None
    export_summary_data = json.loads(export_summary_result[0].text)
    print(f"  Экспорт сессии (summary): {export_summary_data}")
    assert "session_summary" in export_summary_data

    print("\n[Client Test] Тестируем экспорт сессии (json)...")
    try:
        export_json_result = await asyncio.wait_for(
            mcp_client_session.call_tool("export_thinking_session", {"format_type": "json"}),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента export_thinking_session (json) превысил таймаут (20s)")
        
    assert export_json_result is not None
    export_json_data = json.loads(export_json_result[0].text)
    print(f"  Экспорт сессии (json): {export_json_data['thought_count']} thoughts exported.")
    assert "thought_count" in export_json_data
    assert export_json_data["thought_count"] > 0

    print("\n[Client Test] Тестируем экспорт сессии (markdown)...")
    try:
        export_md_result = await asyncio.wait_for(
            mcp_client_session.call_tool("export_thinking_session", {"format_type": "markdown"}),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента export_thinking_session (markdown) превысил таймаут (20s)")
        
    assert export_md_result is not None
    print(f"  Экспорт сессии (markdown): {export_md_result[0].text[:100]}...")
    assert "# Thinking Session Export" in export_md_result[0].text

@pytest.mark.asyncio(loop_scope="module") 
async def test_07_invalid_input_to_enhanced_thinking(mcp_client_session):
    print("\n[Client Test] Тестируем передачу пустого контента мысли...")
    input_data_model = EnhancedThinkingInput(
        thought="",
        thought_type=ThoughtType.OBSERVATION,
        strategy=ThinkingStrategy.LINEAR
    )
    try:
        result = await asyncio.wait_for(
            mcp_client_session.call_tool("enhanced_thinking", pydantic_model_to_dict(input_data_model)),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента enhanced_thinking (пустой ввод) превысил таймаут (20s)")
        
    assert result is not None
    result_data = json.loads(result[0].text)
    print(f"  Результат (пустой ввод): {result_data}")
    assert "error" in result_data.get("input", {})

@pytest.mark.asyncio(loop_scope="module") 
async def test_08_invalid_strategy_adaptation_value(mcp_client_session):
    print("\n[Client Test] Тестируем некорректное значение effectiveness_score...")
    with pytest.raises(ValidationError) as excinfo:
        StrategyAdaptationInput(
            current_strategy=ThinkingStrategy.LINEAR,
            effectiveness_score=1.5,
            context="Error test"
        )
    print(f"  Ожидаемая ошибка валидации Pydantic: {excinfo.value}")
    # FIX: Более общее совпадение для Pydantic v2+
    error_str = str(excinfo.value).lower()
    assert "input should be less than or equal to 1.0" in error_str or "less_than_equal" in error_str


    print("\n[Client Test] Тестируем некорректный тип стратегии.")
    with pytest.raises(ValidationError) as excinfo:
        StrategyAdaptationInput(
            current_strategy="INVALID_STRATEGY",
            effectiveness_score=0.5,
            context="Error test"
        )
    print(f"  Ожидаемая ошибка валидации Pydantic: {excinfo.value}")
    # FIX: Более общее совпадение для Pydantic v2+
    error_str = str(excinfo.value).lower()
    assert "value is not a valid enumeration member" in error_str or ("input should be" in error_str and "invalid_strategy" in error_str)


@pytest.mark.asyncio(loop_scope="module") 
async def test_09_get_thinking_path_non_existent(mcp_client_session):
    print("\n[Client Test] Тестируем получение пути для несуществующей мысли...")
    non_existent_id = "non_existent_thought_12345"
    try:
        path_result = await asyncio.wait_for(
            mcp_client_session.call_tool("get_thinking_path", {"thought_id": non_existent_id}),
            timeout=20 # FIX: Увеличен таймаут
        )
    except asyncio.TimeoutError:
        pytest.fail("Вызов инструмента get_thinking_path (несуществующий ID) превысил таймаут (20s)")
        
    assert path_result is not None
    path_data = json.loads(path_result[0].text)
    print(f"  Результат (несуществующий ID): {path_data}")
    assert "error" in path_data
    assert f"Thought {non_existent_id} not found" in path_data["error"]

@pytest.mark.asyncio(loop_scope="module") 
async def test_10_various_thought_types_and_strategies(mcp_client_session):
    print("\n[Client Test] Тестируем создание мыслей разных типов и стратегий...")
    thoughts_to_create = [
        {"thought": "Наблюдение: Сегодня солнечно.", "type": ThoughtType.OBSERVATION, "strategy": ThinkingStrategy.LINEAR},
        {"thought": "Гипотеза: Если я выпью кофе, то стану более продуктивным.", "type": ThoughtType.HYPOTHESIS, "strategy": ThinkingStrategy.CREATIVE},
        {"thought": "Оценка: Это решение имеет высокие риски, но потенциально большую выгоду.", "type": ThoughtType.EVALUATION, "strategy": ThinkingStrategy.STRATEGIC},
        {"thought": "Вопрос: Как нам оптимизировать процесс?", "type": ThoughtType.QUESTION, "strategy": ThinkingStrategy.DIVERGENT}
    ]

    for item in thoughts_to_create:
        input_data_model = EnhancedThinkingInput(
            thought=item["thought"],
            thought_type=item["type"],
            strategy=item["strategy"]
        )
        try:
            result = await asyncio.wait_for(
                mcp_client_session.call_tool("enhanced_thinking", pydantic_model_to_dict(input_data_model)),
                timeout=20 # FIX: Увеличен таймаут
            )
        except asyncio.TimeoutError:
            pytest.fail(f"Вызов инструмента enhanced_thinking для {item['type']}/{item['strategy']} превысил таймаут (20s)")

        assert result is not None
        result_data = json.loads(result[0].text)
        print(f"  Создана мысль: {result_data['metadata']['thought_type']} ({result_data['metadata']['strategy']})")
        assert result_data["metadata"]["thought_type"] == item["type"].value
        assert result_data["metadata"]["strategy"] == item["strategy"].value
        assert "analysis" in result_data
        assert "thought_id" in result_data