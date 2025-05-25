"""
Тесты для сервера мышления.
Использует базовый класс BaseThinkingTest для тестирования основных функций.
"""

import pytest
import asyncio
from typing import Dict, Any

from tests.base_test import BaseThinkingTest
import enhanced_sequential_thinking_server as es

class TestThinkingServer(BaseThinkingTest):
    """Тесты для сервера мышления."""
    
    @pytest.mark.asyncio
    async def test_create_thought(self):
        """Тест создания мысли."""
        thought = "Это тестовая мысль для проверки функциональности сервера."
        result = await self.create_thought(
            thought=thought,
            thought_type=es.ThoughtType.ANALYSIS,
            strategy=es.ThinkingStrategy.CRITICAL,
            tags=["test", "analysis"]
        )
        
        assert "thought_id" in result, "ID мысли должен быть в ответе"
        assert "analysis" in result, "Анализ должен быть в ответе"
        assert "quality_metrics" in result["analysis"], "Метрики качества должны быть в анализе"
        assert "cognitive_biases" in result["analysis"], "Когнитивные искажения должны быть в анализе"
        
        # Проверяем метрики качества
        metrics = result["analysis"]["quality_metrics"]
        assert "clarity_score" in metrics, "Должен быть показатель ясности"
        assert "logical_coherence" in metrics, "Должна быть логическая связность"
        assert "evidence_strength" in metrics, "Должна быть сила доказательств"
        
        # Сохраняем ID мысли для последующих тестов
        self.thought_id = result["thought_id"]
    
    @pytest.mark.asyncio
    async def test_analyze_session(self):
        """Тест анализа сессии."""
        # Сначала создаем мысль
        await self.create_thought(
            thought="Мысль для анализа сессии.",
            thought_type=es.ThoughtType.OBSERVATION,
            strategy=es.ThinkingStrategy.SYSTEMIC
        )
        
        # Затем анализируем сессию
        result = await self.analyze_session()
        
        assert "coherence_score" in result, "Должен быть показатель связности"
        assert "quality_trend" in result, "Должен быть тренд качества"
        assert "average_quality" in result, "Должно быть среднее качество"
        assert "thought_count" in result, "Должно быть количество мыслей"
    
    @pytest.mark.asyncio
    async def test_metacognitive_reflection(self):
        """Тест метапознавательного размышления."""
        result = await self.metacognitive_reflection(
            focus_area="Общая эффективность мышления",
            analysis_depth=3
        )
        
        assert "thinking_patterns" in result, "Должны быть паттерны мышления"
        assert "strategy_effectiveness" in result, "Должна быть эффективность стратегии"
        assert "cognitive_load" in result, "Должна быть когнитивная нагрузка"
        assert "recommendations" in result, "Должны быть рекомендации"
    
    @pytest.mark.asyncio
    async def test_adapt_strategy(self):
        """Тест адаптации стратегии."""
        result = await self.adapt_strategy(
            current_strategy=es.ThinkingStrategy.CRITICAL,
            effectiveness_score=0.6,
            context="Анализ сложной проблемы",
            constraints=["время", "ресурсы"]
        )
        
        assert "suggested_strategies" in result, "Должны быть предложенные стратегии"
        assert "context_analysis" in result, "Должен быть анализ контекста"
        assert "current_effectiveness" in result, "Должна быть текущая эффективность"
    
    @pytest.mark.asyncio
    async def test_get_thinking_path(self):
        """Тест получения пути мышления."""
        # Сначала создаем мысль
        await self.create_thought(
            thought="Мысль для проверки пути мышления.",
            thought_type=es.ThoughtType.HYPOTHESIS,
            strategy=es.ThinkingStrategy.CREATIVE
        )
        
        # Затем получаем путь мышления
        result = await self.get_thinking_path()
        
        assert "path" in result, "Должен быть путь мышления"
        assert "thought_id" in result, "Должен быть ID мысли"
        assert "path_length" in result, "Должна быть длина пути"
        
        if result["path"]:
            first_thought = result["path"][0]
            assert "step" in first_thought, "Должен быть шаг"
            assert "content" in first_thought, "Должно быть содержание"
            assert "type" in first_thought, "Должен быть тип"
            assert "strategy" in first_thought, "Должна быть стратегия"
    
    @pytest.mark.asyncio
    async def test_export_session(self):
        """Тест экспорта сессии."""
        # Создаем несколько мыслей
        await self.create_thought(
            thought="Первая мысль для экспорта.",
            thought_type=es.ThoughtType.ANALYSIS,
            strategy=es.ThinkingStrategy.SYSTEMATIC
        )
        await self.create_thought(
            thought="Вторая мысль для экспорта.",
            thought_type=es.ThoughtType.EVALUATION,
            strategy=es.ThinkingStrategy.CRITICAL
        )
        
        # Экспортируем в разных форматах
        for format_type in ["json", "markdown", "summary"]:
            result = await self.export_session(format_type=format_type)
            
            if format_type == "json":
                assert "thoughts" in result, "Должны быть мысли в JSON"
                assert "session_id" in result, "Должен быть ID сессии"
            elif format_type == "markdown":
                assert isinstance(result.get("content", ""), str), "Контент должен быть строкой"
                assert "#" in result.get("content", ""), "Должен быть заголовок в markdown"
            elif format_type == "summary":
                assert "session_summary" in result, "Должно быть резюме сессии"
                assert "key_insights" in result, "Должны быть ключевые инсайты"
    
    @pytest.mark.asyncio
    async def test_list_tools(self):
        """Тест получения списка инструментов с сервера."""
        tools = await self.list_tools()
        assert isinstance(tools, list), "Список инструментов должен быть списком"
        assert len(tools) > 0, "Сервер должен возвращать хотя бы один инструмент"
        print("Доступные инструменты:", tools)

async def run_tests():
    """Запускает все тесты."""
    # Настраиваем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Создаем и запускаем тесты
    test = TestThinkingServer()
    await test.test_full_workflow()

if __name__ == "__main__":
    asyncio.run(run_tests()) 