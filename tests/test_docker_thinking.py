"""
Тесты для сервера мышления в Docker.
Использует базовый класс для тестирования основных функций в контейнере.
"""

import asyncio
import logging
from typing import Dict

from tests.base_test import BaseThinkingTest

logger = logging.getLogger(__name__)

class TestDockerThinking(BaseThinkingTest):
    """Тесты для сервера мышления в Docker."""
    
    async def test_docker_workflow(self):
        """Тестирует полный рабочий процесс сервера мышления в Docker."""
        try:
            # Тест 1: Создание мысли о тестировании
            logger.info("Создаем мысль о важности тестирования...")
            result = await self.create_thought(
                thought="Тестирование программного обеспечения является критически важным процессом, который помогает выявлять ошибки и обеспечивать качество кода. Без надлежащего тестирования даже хорошо написанный код может содержать скрытые проблемы, которые могут привести к серьезным последствиям в продакшене. Автоматизированное тестирование, включая модульные, интеграционные и end-to-end тесты, позволяет быстро обнаруживать регрессии и обеспечивать стабильность приложения.",
                tags=["тестирование", "качество", "разработка"]
            )
            logger.info(f"Результат создания мысли: {result}")
            
            # Тест 2: Анализ сессии
            logger.info("Анализируем сессию...")
            session_result = await self.analyze_session()
            logger.info(f"Анализ сессии: {session_result}")
            
            # Тест 3: Получение пути мышления
            logger.info("Получаем путь мышления...")
            path_result = await self.get_thinking_path()
            logger.info(f"Путь мышления: {path_result}")
            
            # Тест 4: Экспорт сессии
            logger.info("Экспортируем сессию...")
            export_result = await self.export_session(format_type="summary")
            logger.info(f"Результат экспорта: {export_result}")
            
        except Exception as e:
            logger.error(f"Ошибка при выполнении тестов в Docker: {e}", exc_info=True)
            raise

async def run_docker_tests():
    """Запускает все тесты в Docker."""
    # Настраиваем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Создаем и запускаем тесты
    test = TestDockerThinking()
    await test.test_docker_workflow()

if __name__ == "__main__":
    asyncio.run(run_docker_tests()) 