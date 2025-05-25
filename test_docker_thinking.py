import asyncio
from fastmcp import FastMCP
from mcp.types import EnhancedThinkingInput, ThinkingStrategy, ThoughtType

async def test_enhanced_thinking():
    # Создаем клиент MCP с URL нашего сервера в Docker
    client = FastMCP("enhanced-sequential-thinking-server")
    client.base_url = "http://localhost:8000"
    
    try:
        # Создаем мысль о важности тестирования
        print("\nСоздаем мысль о важности тестирования...")
        input_data = EnhancedThinkingInput(
            thought="Тестирование программного обеспечения является критически важным процессом, который помогает выявлять ошибки и обеспечивать качество кода. Без надлежащего тестирования даже хорошо написанный код может содержать скрытые проблемы, которые могут привести к серьезным последствиям в продакшене. Автоматизированное тестирование, включая модульные, интеграционные и end-to-end тесты, позволяет быстро обнаруживать регрессии и обеспечивать стабильность приложения.",
            thought_type=ThoughtType.ANALYSIS,
            strategy=ThinkingStrategy.CRITICAL,
            tags=["тестирование", "качество", "разработка"],
            request_analysis=True,
            request_validation=True
        )
        
        # Вызываем инструмент enhanced_thinking
        result = await client.call_tool("enhanced_thinking", input_data)
        print("\nРезультат анализа мысли:")
        print(result[0].text)
        
        # Получаем ID созданной мысли для последующих тестов
        thought_data = eval(result[0].text)
        thought_id = thought_data.get("thought_id")
        
        if thought_id:
            # Тест 2: Анализ сессии
            print("\nАнализируем сессию мышления...")
            session_result = await client.call_tool("analyze_thinking_session")
            print("\nРезультат анализа сессии:")
            print(session_result[0].text)
            
            # Тест 3: Получение пути мышления
            print("\nПолучаем путь мышления...")
            path_result = await client.call_tool("get_thinking_path", thought_id)
            print("\nПуть мышления:")
            print(path_result[0].text)
            
            # Тест 4: Экспорт сессии
            print("\nЭкспортируем сессию...")
            export_result = await client.call_tool("export_thinking_session", format_type="summary")
            print("\nЭкспорт сессии:")
            print(export_result[0].text)
        
    except Exception as e:
        print(f"\nПроизошла ошибка при тестировании: {str(e)}")
        raise

if __name__ == "__main__":
    print("Начинаем тестирование сервера мышления в Docker...")
    asyncio.run(test_enhanced_thinking()) 