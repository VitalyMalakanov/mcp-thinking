DEFAULT_LANG = "en"

LANGUAGES = ["en", "ru"]

TRANSLATIONS = {
    "en": {
        # General UI/Display
        
        "THOUGHT": "Thought",
        "ID": "ID",
        "Branch": "Branch",
        "Revises": "Revises",
        "Strategy": "Strategy",
        "Strategy Description": "Strategy Description",
        "Connections": "Connections",
        "Supports": "Supports",
        "Contradicts": "Contradicts",
        "Builds on": "Builds on",
        "No connections": "No connections",
        "Biases": "Biases",
        "None detected": "None detected",
        "Tags": "Tags",
        "No tags": "No tags",
        "Clarity": "Clarity",
        "Logic": "Logic",
        "Evidence": "Evidence",
        "Novelty": "Novelty",
        "Confidence": "Confidence",
        "Strategy Score": "Strategy Score",
        "SESSION ANALYSIS": "SESSION ANALYSIS",
        "Coherence Score": "Coherence Score",
        "Quality Trend": "Quality Trend",
        "Average Quality": "Average Quality",
        "Thought Count": "Thought Count",
        "Cognitive Biases": "Cognitive Biases",
        "LOGICAL CONFLICTS DETECTED": "LOGICAL CONFLICTS DETECTED",
        "METACOGNITIVE ANALYSIS": "METACOGNITIVE ANALYSIS",
        "Focus Area": "Focus Area",
        "Dominant Thought Type": "Dominant Thought Type",
        "Dominant Strategy": "Dominant Strategy",
        "Strategy Effectiveness": "Strategy Effectiveness",
        "Cognitive Load": "Cognitive Load",
        "RECOMMENDATIONS": "RECOMMENDATIONS",
        "STRATEGY ADAPTATION": "STRATEGY ADAPTATION",
        "Current Strategy": "Current Strategy",
        "Effectiveness": "Effectiveness",
        "Context": "Context",
        "Suggested Strategies": "Suggested Strategies",
        "THINKING PATH": "THINKING PATH",
        "step": "step",
        "content": "content",
        "type": "type",
        "quality_score": "quality_score", # Short for display
        "QUALITY_SCORE_SHORT": "Q",
        "INFO_SERVER_HEALTHY": "Server is healthy", # Abbreviation for quality score in path display

        # Errors & Warnings
        "WARNING_ANALYSIS_LIBS_NOT_FOUND": "WARNING: Advanced analysis libraries not found. Install numpy, scikit-learn, textstat for enhanced features.",
        "WARNING_COLORAMA_NOT_FOUND": "WARNING: colorama not found. Install with 'pip install colorama' for colored output.",
        "ERROR_MCP_SDK_IMPORT_FAILED": "ERROR: Failed to import MCP SDK",
        "WARNING_PATCH_RUNTIME_ERROR_CAUGHT": "Patch: Caught RuntimeError: Server not initialized. Retrying after a short delay.",
        "ERROR_PATCH_APPLY_FAILED": "Error applying patch",
        "ERROR_COMPONENTS_NOT_INIT": "Required components not initialized",
        "ERROR_INIT_FAILED": "Initialization failed",
        "ERROR_INIT_TIMEOUT": "Server initialization timeout",
        "ERROR_INIT_WAIT_ERROR": "Error during initialization wait",
        "ERROR_INPUT_VALIDATION_ERROR_PREFIX": "Input validation error in",
        "ERROR_TOOL_EXECUTION_FAILED_PREFIX": "Error in",
        "ERROR_EMPTY_THOUGHT_CONTENT": "Empty thought content",
        "ERROR_FAILED_TO_CREATE_THOUGHT": "Failed to create thought",
        "ERROR_SESSION_NOT_FOUND": "Session not found",
        "ERROR_UNSUPPORTED_FORMAT": "Unsupported format",
        "ERROR_LOGICAL_CONSISTENCY_CHECK_FAILED": "Error checking logical consistency",
        "ERROR_UNHANDLED_MIDDLEWARE_ERROR": "Unhandled error in middleware",
        "INTERNAL_SERVER_ERROR_MESSAGE": "An internal server error occurred.",
        "ERROR_UNEXPECTED_SERVER_ERROR": "An unexpected error occurred during server operation:",

        # Info messages
        "INFO_MCP_SDK_IMPORTED": "[*] MCP SDK components imported successfully.",
        "INFO_PATCH_APPLIED": "[*] Patch for RuntimeError workaround applied.",
        "INFO_SERVER_INIT_COMPLETED": "Server initialization completed successfully",
        "INFO_COMPONENT_VALIDATION_SUCCESS": "Component validation completed successfully",
        "INFO_COMPONENT_VALIDATION_FAILED": "Component validation failed",
        "INFO_WAITING_INIT": "Waiting for server initialization...",
        "INFO_SERVER_INIT_DONE": "Server initialization completed",
        "INFO_SERVER_STARTING": "[*] Starting Enhanced MCP server '{name}'...",
        "INFO_AVAILABLE_TOOLS": "[*] Available tools:",
        "INFO_SERVER_LISTENING": "[*] Server listening on http://{address}:{port}/sse",
        "INFO_PRESS_CTRL_C_TO_STOP": "[*] Press Ctrl+C to stop",
        "INFO_SERVER_STOPPED_BY_USER": "\n[*] Server stopped by user.",
        "INFO_CALL_LOG_GENERIC": "[*] called", # Generic part of "tool_name called"
        "THOUGHT_NOT_FOUND": "Thought {thought_id} not found",

        # Strategy reasoning messages
        "HIGH_COMPLEXITY_REASON": "High complexity requires a systemic approach",
        "DETAILED_ANALYSIS_NEEDED_REASON": "Detailed analysis of components is needed",
        "AMBIGUITY_CRITICAL_ANALYSIS_REASON": "Ambiguity requires critical analysis",
        "OPPOSING_VIEWPOINTS_REASON": "Consideration of opposing viewpoints",
        "EMOTIONAL_CONTEXT_EMPATHETIC_REASON": "Emotional context requires an empathetic approach",
        "REFLECTION_NEEDED_REASON": "Reflection on emotional aspects is needed",
        "STRATEGY_EFFECTIVE_PREVIOUSLY_REASON": "This strategy was effective in similar situations",
        "EXPLORE_ALTERNATIVES_REASON": "Try exploring alternative directions",
        "ANALYZE_APPROACH_REASON": "Analyze your approach to the solution",
        "USE_SYSTEMATIC_ANALYSIS_REASON": "Use systematic analysis",
        "APPLY_STRICT_LOGIC_REASON": "Apply strict logical analysis",
        "TRY_CREATIVE_APPROACH_REASON": "Try a creative approach",
        "GENERATE_MORE_ALTERNATIVES_REASON": "Generate more alternatives",
        "RECOMMENDATION_REASONING_SUFFIX": "Recommendations are based on context analysis and effectiveness history",

        # Metacognition recommendations
        "RECOMMENDATION_BREAK_DOWN_TASK": "Consider breaking down complex tasks into simpler sub-tasks",
        "RECOMMENDATION_BIASES_ATTENTION": "Pay attention to cognitive biases in reasoning",
        "RECOMMENDATION_STRATEGY_INEFFECTIVE": "The current thinking strategy might be ineffective, consider alternatives",

        # Export fields
        "EXPORT_SESSION_ID": "Session ID",
        "EXPORT_DATE": "Export Date",
        "EXPORT_TOTAL_THOUGHTS": "Total Thoughts",
        "EXPORT_SESSION_TITLE": "Thinking Session Export",
        "EXPORT_THOUGHTS_HEADING": "Thoughts",
        "AVERAGE_QUALITY_MARKDOWN": "Quality",
        "DETECTED_BIASES_MARKDOWN": "Detected Biases",

        # Summary insights
        "SUMMARY_PROCESSED_THOUGHTS": "Processed {count} thoughts with {score:.2f} coherence",
        "SUMMARY_QUALITY_TREND": "Quality trend: {trend}",
        "QUALITY_TREND_IMPROVING": "Improving",
        "QUALITY_TREND_DECLINING": "Declining",
        "QUALITY_TREND_STABLE": "Stable",
        "SUMMARY_DETECTED_BIASES": "Detected {count} cognitive biases",

        # Misc internal strings
        "DESCRIPTION_UNAVAILABLE": "Description unavailable",
        "semantic_contradiction": "semantic_contradiction",
        "Unknown": "Unknown", # for conflict type
        "GENERAL_FOCUS_AREA": "General", # for metacognition focus area
        "UNKNOWN_CONFLICT_TYPE": "Unknown Conflict Type",
        "THOUGHT_HEADER_ID": "ID",
        "THOUGHT_HEADER_BRANCH": "Branch",
        "THOUGHT_HEADER_REVISES": "Revises",
        "CONNECTIONS_LABEL": "Connections",
        "BIASES_LABEL": "Biases",
        "TAGS_LABEL": "Tags",

        # Tool names for logging
        "TOOL_NAME_ENHANCED_THINKING": "enhanced_thinking",
        "TOOL_NAME_ANALYZE_SESSION": "analyze_thinking_session",
        "TOOL_NAME_METACOGNITIVE_REFLECTION": "metacognitive_reflection",
        "TOOL_NAME_ADAPT_STRATEGY": "adapt_thinking_strategy",
        "TOOL_NAME_GET_PATH": "get_thinking_path",
        "TOOL_NAME_EXPORT_SESSION": "export_thinking_session",

        # Domain analysis
        "TEXT_DOMAIN_PROGRAMMING": "programming",
        "TEXT_DOMAIN_BUSINESS": "business",
        "TEXT_DOMAIN_SCIENCE": "science",
        "TEXT_DOMAIN_GENERAL": "general",
    },
    "ru": {
        # General UI/Display
        "THOUGHT": "Мысль",
        "INFO_SERVER_HEALTHY": "Сервер работает корректно",
        "ID": "ID",
        "Branch": "Ветка",
        "Revises": "Пересматривает",
        "Strategy": "Стратегия",
        "Strategy Description": "Описание стратегии",
        "Connections": "Связи",
        "Supports": "Поддерживает",
        "Contradicts": "Противоречит",
        "Builds on": "Развивает",
        "No connections": "Нет связей",
        "Biases": "Когнитивные искажения",
        "None detected": "Не обнаружено",
        "Tags": "Теги",
        "No tags": "Нет тегов",
        "Clarity": "Ясность",
        "Logic": "Логика",
        "Evidence": "Доказательность",
        "Novelty": "Новизна",
        "Confidence": "Уверенность",
        "Strategy Score": "Оценка стратегии",
        "SESSION ANALYSIS": "АНАЛИЗ СЕССИИ",
        "Coherence Score": "Оценка связности",
        "Quality Trend": "Тренд качества",
        "Average Quality": "Среднее качество",
        "Thought Count": "Количество мыслей",
        "Cognitive Biases": "Когнитивные искажения",
        "LOGICAL CONFLICTS DETECTED": "ОБНАРУЖЕНЫ ЛОГИЧЕСКИЕ КОНФЛИКТЫ",
        "METACOGNITIVE ANALYSIS": "МЕТАКОГНИТИВНЫЙ АНАЛИЗ",
        "Focus Area": "Область фокуса",
        "Dominant Thought Type": "Доминирующий тип мысли",
        "Dominant Strategy": "Доминирующая стратегия",
        "Strategy Effectiveness": "Эффективность стратегии",
        "Cognitive Load": "Когнитивная нагрузка",
        "RECOMMENDATIONS": "РЕКОМЕНДАЦИИ",
        "STRATEGY ADAPTATION": "АДАПТАЦИЯ СТРАТЕГИИ",
        "Current Strategy": "Текущая стратегия",
        "Effectiveness": "Эффективность",
        "Context": "Контекст",
        "Suggested Strategies": "Рекомендуемые стратегии",
        "THINKING PATH": "ПУТЬ МЫШЛЕНИЯ",
        "step": "шаг",
        "content": "содержание",
        "type": "тип",
        "quality_score": "оценка_качества", # Short for display
        "QUALITY_SCORE_SHORT": "К", # Abbreviation for quality score in path display

        # Errors & Warnings
        "WARNING_ANALYSIS_LIBS_NOT_FOUND": "ВНИМАНИЕ: Библиотеки для расширенного анализа не найдены. Установите numpy, scikit-learn, textstat для расширенных функций.",
        "WARNING_COLORAMA_NOT_FOUND": "ВНИМАНИЕ: colorama не найден. Установите 'pip install colorama' для цветного вывода.",
        "ERROR_MCP_SDK_IMPORT_FAILED": "ОШИБКА: Не удалось импортировать MCP SDK",
        "WARNING_PATCH_RUNTIME_ERROR_CAUGHT": "Патч: Перехвачена RuntimeError: Сервер не инициализирован. Повторная попытка после короткой задержки.",
        "ERROR_PATCH_APPLY_FAILED": "Ошибка применения патча",
        "ERROR_COMPONENTS_NOT_INIT": "Необходимые компоненты не инициализированы",
        "ERROR_INIT_FAILED": "Инициализация не удалась",
        "ERROR_INIT_TIMEOUT": "Тайм-аут инициализации сервера",
        "ERROR_INIT_WAIT_ERROR": "Ошибка во время ожидания инициализации",
        "ERROR_INPUT_VALIDATION_ERROR_PREFIX": "Ошибка валидации ввода в",
        "ERROR_TOOL_EXECUTION_FAILED_PREFIX": "Ошибка в",
        "ERROR_EMPTY_THOUGHT_CONTENT": "Пустое содержание мысли",
        "ERROR_FAILED_TO_CREATE_THOUGHT": "Не удалось создать мысль",
        "ERROR_SESSION_NOT_FOUND": "Сессия не найдена",
        "ERROR_UNSUPPORTED_FORMAT": "Неподдерживаемый формат",
        "ERROR_LOGICAL_CONSISTENCY_CHECK_FAILED": "Ошибка проверки логической согласованности",
        "ERROR_UNHANDLED_MIDDLEWARE_ERROR": "Необработанная ошибка в middleware",
        "INTERNAL_SERVER_ERROR_MESSAGE": "Произошла внутренняя ошибка сервера.",
        "ERROR_UNEXPECTED_SERVER_ERROR": "Произошла неожиданная ошибка при работе сервера:",

        # Info messages
        "INFO_MCP_SDK_IMPORTED": "[*] Компоненты MCP SDK успешно импортированы.",
        "INFO_PATCH_APPLIED": "[*] Патч для обхода RuntimeError применен.",
        "INFO_SERVER_INIT_COMPLETED": "Инициализация сервера успешно завершена",
        "INFO_COMPONENT_VALIDATION_SUCCESS": "Проверка компонентов успешно завершена",
        "INFO_COMPONENT_VALIDATION_FAILED": "Проверка компонентов не удалась",
        "INFO_WAITING_INIT": "Ожидание инициализации сервера...",
        "INFO_SERVER_INIT_DONE": "Инициализация сервера завершена",
        "INFO_SERVER_STARTING": "[*] Запуск Enhanced MCP сервера '{name}'...",
        "INFO_AVAILABLE_TOOLS": "[*] Доступные инструменты:",
        "INFO_SERVER_LISTENING": "[*] Сервер слушает на http://{address}:{port}/sse",
        "INFO_PRESS_CTRL_C_TO_STOP": "[*] Для остановки нажмите Ctrl+C",
        "INFO_SERVER_STOPPED_BY_USER": "\n[*] Сервер остановлен пользователем.",
        "INFO_CALL_LOG_GENERIC": "[*] вызван", # Generic part of "tool_name called"
        "THOUGHT_NOT_FOUND": "Мысль {thought_id} не найдена",

        # Strategy reasoning messages
        "HIGH_COMPLEXITY_REASON": "Высокая сложность требует системного подхода",
        "DETAILED_ANALYSIS_NEEDED_REASON": "Необходим детальный анализ компонентов",
        "AMBIGUITY_CRITICAL_ANALYSIS_REASON": "Неоднозначность требует критического анализа",
        "OPPOSING_VIEWPOINTS_REASON": "Рассмотрение противоположных точек зрения",
        "EMOTIONAL_CONTEXT_EMPATHETIC_REASON": "Эмоциональный контекст требует эмпатического подхода",
        "REFLECTION_NEEDED_REASON": "Необходима рефлексия эмоциональных аспектов",
        "STRATEGY_EFFECTIVE_PREVIOUSLY_REASON": "Эта стратегия была эффективна в похожих ситуациях",
        "EXPLORE_ALTERNATIVES_REASON": "Попробуйте исследовать альтернативные направления",
        "ANALYZE_APPROACH_REASON": "Проанализируйте ваш подход к решению",
        "USE_SYSTEMATIC_ANALYSIS_REASON": "Используйте систематический анализ",
        "APPLY_STRICT_LOGIC_REASON": "Примените строгий логический анализ",
        "TRY_CREATIVE_APPROACH_REASON": "Попробуйте креативный подход",
        "GENERATE_MORE_ALTERNATIVES_REASON": "Генерируйте больше альтернатив",
        "RECOMMENDATION_REASONING_SUFFIX": "Рекомендации основаны на анализе контекста и истории эффективности",

        # Metacognition recommendations
        "RECOMMENDATION_BREAK_DOWN_TASK": "Рассмотрите разбиение сложной задачи на более простые подзадачи",
        "RECOMMENDATION_BIASES_ATTENTION": "Обратите внимание на когнитивные искажения в рассуждениях",
        "RECOMMENDATION_STRATEGY_INEFFECTIVE": "Текущая стратегия мышления может быть неэффективной, рассмотрите альтернативы",

        # Export fields
        "EXPORT_SESSION_ID": "ID Сессии",
        "EXPORT_DATE": "Дата Экспорта",
        "EXPORT_TOTAL_THOUGHTS": "Всего Мыслей",
        "EXPORT_SESSION_TITLE": "Экспорт Сессии Мышления",
        "EXPORT_THOUGHTS_HEADING": "Мысли",
        "AVERAGE_QUALITY_MARKDOWN": "Качество",
        "DETECTED_BIASES_MARKDOWN": "Обнаруженные искажения",

        # Summary insights
        "SUMMARY_PROCESSED_THOUGHTS": "Обработано {count} мыслей со связностью {score:.2f}",
        "SUMMARY_QUALITY_TREND": "Тренд качества: {trend}",
        "QUALITY_TREND_IMPROVING": "Улучшается",
        "QUALITY_TREND_DECLINING": "Ухудшается",
        "QUALITY_TREND_STABLE": "Стабильный",
        "SUMMARY_DETECTED_BIASES": "Обнаружено {count} когнитивных искажений",

        # Misc internal strings
        "DESCRIPTION_UNAVAILABLE": "Описание недоступно",
        "semantic_contradiction": "семантическое_противоречие",
        "Unknown": "Неизвестно", # for conflict type
        "GENERAL_FOCUS_AREA": "Общее", # for metacognition focus area
        "UNKNOWN_CONFLICT_TYPE": "Неизвестный тип конфликта",
        "THOUGHT_HEADER_ID": "ID",
        "THOUGHT_HEADER_BRANCH": "Ветка",
        "THOUGHT_HEADER_REVISES": "Пересматривает",
        "CONNECTIONS_LABEL": "Связи",
        "BIASES_LABEL": "Искажения",
        "TAGS_LABEL": "Теги",

        # Tool names for logging
        "TOOL_NAME_ENHANCED_THINKING": "enhanced_thinking",
        "TOOL_NAME_ANALYZE_SESSION": "analyze_thinking_session",
        "TOOL_NAME_METACOGNITIVE_REFLECTION": "metacognitive_reflection",
        "TOOL_NAME_ADAPT_STRATEGY": "adapt_thinking_strategy",
        "TOOL_NAME_GET_PATH": "get_thinking_path",
        "TOOL_NAME_EXPORT_SESSION": "export_thinking_session",

        # Domain analysis
        "TEXT_DOMAIN_PROGRAMMING": "программирование",
        "TEXT_DOMAIN_BUSINESS": "бизнес",
        "TEXT_DOMAIN_SCIENCE": "наука",
        "TEXT_DOMAIN_GENERAL": "общее",
    }
}

def t(key, lang=DEFAULT_LANG, **kwargs):
    """
    Функция перевода по ключу и языку (en по умолчанию).
    Поддерживает базовую подстановку {placeholders} из kwargs.
    """
    translation_dict = TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANG])
    translated_text = translation_dict.get(key, key) # Fallback to key if not found

    # Apply kwargs for dynamic formatting if any are provided
    if kwargs:
        try:
            return translated_text.format(**kwargs)
        except KeyError as e:
            # Handle cases where placeholder in string doesn't match kwargs
            print(f"WARNING: Missing placeholder '{e}' for key '{key}' in language '{lang}'. Returning raw translated text.", file=sys.stderr)
            return translated_text
        except IndexError as e:
            # Handle potential issues with positional formatting if it were used
            print(f"WARNING: Positional formatting error for key '{key}' in language '{lang}'. Returning raw translated text.", file=sys.stderr)
            return translated_text
    return translated_text