import asyncio
from fastmcp import FastMCP
from mcp.types import EnhancedThinkingInput, MetacognitionInput, StrategyAdaptationInput
from mcp.types import ThinkingStrategy, ThoughtType

async def test_enhanced_thinking():
    # Создаем клиент с указанием URL сервера
    client = FastMCP("enhanced-sequential-thinking-server")
    client.base_url = "http://localhost:8000"  # Добавляем URL сервера
    
    try:
        # Тест 1: Создание базовой мысли
        print("\nТестируем создание мысли...")
        input_data = EnhancedThinkingInput(
            thought="Искусственный интеллект может значительно улучшить процесс принятия решений, но требует тщательного контроля и этических рамок.",
            thought_type=ThoughtType.ANALYSIS,
            strategy=ThinkingStrategy.CRITICAL,
            tags=["AI", "этика", "принятие решений"]
        )
        
        result = await client.call_tool("enhanced_thinking", input_data)
        print("\nРезультат создания мысли:")
        print(result[0].text)
        
        # Получаем ID созданной мысли для последующих тестов
        thought_data = eval(result[0].text)
        thought_id = thought_data.get("thought_id")
        
        # Тест 2: Анализ сессии
        print("\nТестируем анализ сессии...")
        session_result = await client.call_tool("analyze_thinking_session")
        print("\nАнализ сессии:")
        print(session_result[0].text)
        
        # Тест 3: Метапознавательное размышление
        print("\nТестируем метапознавательное размышление...")
        meta_input = MetacognitionInput(
            focus_area="Эффективность критического мышления",
            analysis_depth=3
        )
        meta_result = await client.call_tool("metacognitive_reflection", meta_input)
        print("\nМетапознавательный анализ:")
        print(meta_result[0].text)
        
        # Тест 4: Адаптация стратегии
        print("\nТестируем адаптацию стратегии...")
        strategy_input = StrategyAdaptationInput(
            current_strategy=ThinkingStrategy.CRITICAL,
            effectiveness_score=0.7,
            context="Анализ этических аспектов ИИ",
            constraints=["время", "ресурсы"]
        )
        strategy_result = await client.call_tool("adapt_thinking_strategy", strategy_input)
        print("\nАдаптация стратегии:")
        print(strategy_result[0].text)
        
        # Тест 5: Получение пути мышления
        if thought_id:
            print("\nТестируем получение пути мышления...")
            path_result = await client.call_tool("get_thinking_path", thought_id)
            print("\nПуть мышления:")
            print(path_result[0].text)
        
        # Тест 6: Экспорт сессии
        print("\nТестируем экспорт сессии...")
        export_result = await client.call_tool("export_thinking_session", format_type="summary")
        print("\nЭкспорт сессии:")
        print(export_result[0].text)
        
    except Exception as e:
        print(f"\nПроизошла ошибка при тестировании: {str(e)}")
        raise

if __name__ == "__main__":
    print("Начинаем тестирование сервера мышления...")
    asyncio.run(test_enhanced_thinking()) 