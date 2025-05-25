"""
Language-dependent markers and patterns for thought quality analysis and cognitive strategies.
"""

COGNITIVE_BIAS_MARKERS = {
    "en": {
        "confirmation bias": {
            "markers": [
                "always", "never", "absolutely", "definitely",
                "undoubtedly", "unquestionably", "obviously"
            ],
            "context": ["assertion", "without evidence"]
        },
        "black-and-white thinking": {
            "markers": [
                "either", "or", "only", "exclusively",
                "all", "nothing", "completely"
            ],
            "context": ["extremes", "lack of nuance"]
        },
        "emotional reasoning": {
            "markers": [
                "feel", "seems", "sense", "think",
                "believe", "hope", "fear"
            ],
            "context": ["emotions", "without facts"]
        },
        "hasty generalization": {
            "markers": [
                "all", "every", "no one", "always",
                "never", "everywhere", "nowhere"
            ],
            "context": ["generalization", "few examples"]
        }
    },
    "ru": {
        "подтверждающее искажение": {
            "markers": [
                "всегда", "никогда", "абсолютно", "точно",
                "безусловно", "несомненно", "очевидно"
            ],
            "context": ["утверждение", "без доказательств"]
        },
        "черно-белое мышление": {
            "markers": [
                "либо", "или", "только", "исключительно",
                "все", "ничего", "полностью"
            ],
            "context": ["крайности", "отсутствие градаций"]
        },
        "эмоциональное рассуждение": {
            "markers": [
                "чувствую", "кажется", "ощущаю", "думаю",
                "верю", "надеюсь", "боюсь"
            ],
            "context": ["эмоции", "без фактов"]
        },
        "поспешные обобщения": {
            "markers": [
                "все", "каждый", "никто", "всегда",
                "никогда", "везде", "нигде"
            ],
            "context": ["обобщение", "мало примеров"]
        }
    }
}

CONTRADICTION_WORDS = {
    "en": [
        ("not", "yes"), ("no", "yes"), ("bad", "good"),
        ("impossible", "possible"), ("incorrect", "correct")
    ],
    "ru": [
        ("не", "да"), ("нет", "да"), ("плохо", "хорошо"),
        ("невозможно", "возможно"), ("неверно", "верно")
    ]
}

LOGICAL_CONNECTORS = {
    "en": [
        "therefore", "consequently", "thus", "as a result",
        "however", "but", "nevertheless", "on the other hand",
        "firstly", "secondly", "additionally", "moreover"
    ],
    "ru": [
        "поэтому", "следовательно", "таким образом", "в результате",
        "однако", "но", "тем не менее", "с другой стороны",
        "во-первых", "во-вторых", "кроме того", "более того"
    ]
}

EVIDENCE_PATTERNS = {
    "en": [
        r'\d+%', r'\d+\.\d+', r'research', r'data', r'statistics',
        r'fact', r'evidence', r'example', r'case'
    ],
    "ru": [
        r'\d+%', r'\d+\.\d+', r'исследование', r'данные', r'статистика',
        r'факт', r'доказательство', r'пример', r'случай'
    ]
}

UNCERTAINTY_MARKERS = {
    "en": ["possibly", "probably", "seems", "might be", "I assume"],
    "ru": ["возможно", "вероятно", "кажется", "может быть", "предположу"]
}

CERTAINTY_MARKERS = {
    "en": ["definitely", "surely", "undoubtedly", "obviously", "unquestionably"],
    "ru": ["определенно", "точно", "безусловно", "очевидно", "несомненно"]
}

CRITICAL_MARKERS = {
    "en": {
        "argumentation": [
            "because", "therefore", "thus",
            "this proves", "based on", "stemming from"
        ],
        "evaluation": [
            "reliability", "validity", "justification",
            "verification", "confirmation", "substantiation"
        ],
        "analysis": [
            "consider", "analyze", "investigate",
            "break down", "examine", "evaluate"
        ],
        "refutation": [
            "refutes", "contradicts", "inconsistent with",
            "raises doubts", "requires verification"
        ],
        "structure_keywords": [ # Used in _analyze_critical_thinking for bonus
            ("if", "then"), ("although", "but"), ("despite", "yet")
        ]
    },
    "ru": {
        "argumentation": [
            "потому что", "следовательно", "таким образом",
            "это доказывает", "на основе", "исходя из"
        ],
        "оценка": [
            "надежность", "достоверность", "обоснованность",
            "проверка", "верификация", "подтверждение"
        ],
        "анализ": [
            "рассмотрим", "проанализируем", "исследуем",
            "разберем", "изучим", "оценим"
        ],
        "опровержение": [
            "опровергает", "противоречит", "не согласуется",
            "вызывает сомнения", "требует проверки"
        ],
        "structure_keywords": [ # Used in _analyze_critical_thinking for bonus
            ("если", "то"), ("хотя", "но"), ("несмотря на", "все же")
        ]
    }
}
SYSTEMIC_MARKERS = {
    "en": {
        "interconnections": [
            "interconnection", "link between", "affects", "depends on",
            "components", "system elements"
        ],
        "structure": [
            "structure", "organization", "hierarchy", "subsystem"
        ],
        "dynamics": [
            "cycle", "feedback loop", "system behavior", "emergence"
        ],
        "boundaries": [
            "system boundaries", "external environment", "internal factors"
        ],
        "causal_keywords": [ # Used in _analyze_systemic_thinking for bonus
            "cause", "effect", "leads to"
        ]
    },
    "ru": {
        "interconnections": [
            "взаимосвязь", "связь между", "влияет на", "зависит от",
            "компоненты", "элементы системы"
        ],
        "structure": [
            "структура", "организация", "иерархия", "подсистема"
        ],
        "dynamics": [
            "цикл", "обратная связь", "поведение системы", "эмерджентность"
        ],
        "boundaries": [
            "границы системы", "внешняя среда", "внутренние факторы"
        ],
        "causal_keywords": [ # Used in _analyze_systemic_thinking for bonus
            "причина", "следствие", "приводит к"
        ]
    }
}
LATERAL_MARKERS = {
    "en": {
        "analogies": ["analogy", "similar to", "as if", "metaphor"],
        "re-framing": ["re-evaluate", "new perspective", "unconventional", "different view"],
        "provocation": ["what if", "imagine", "and if"],
        "random associations": ["random word", "unrelated", "sudden idea"],
        "question_phrases": ["why not", "what if"] # Used in _analyze_lateral_thinking for bonus
    },
    "ru": {
        "аналогии": ["аналогия", "похоже на", "как будто", "метафора"],
        "переосмысление": ["переосмыслить", "по-новому", "нестандартно", "другой взгляд"],
        "провокация": ["что если", "представим", "а если бы"],
        "случайные ассоциации": ["случайное слово", "не связано", "внезапная идея"],
        "question_phrases": ["почему бы не", "а что если"] # Used in _analyze_lateral_thinking for bonus
    }
}
STRATEGIC_MARKERS = {
    "en": {
        "goals": ["goal", "objective", "outcome", "achieve"],
        "planning": ["plan", "strategy", "stages", "actions", "steps"],
        "future": ["long-term", "perspective", "future", "forecast", "scenario"],
        "resources": ["resources", "budget", "time", "people", "assets"],
        "risks_opportunities": ["risk", "opportunity", "threat", "potential"],
        "priority_keywords": ["priority", "choice"] # Used in _analyze_strategic_thinking for bonus
    },
    "ru": {
        "цели": ["цель", "задача", "результат", "достичь"],
        "планирование": ["план", "стратегия", "этапы", "действия", "шаги"],
        "будущее": ["долгосрочный", "перспектива", "будущее", "прогноз", "сценарий"],
        "ресурсы": ["ресурсы", "бюджет", "время", "люди", "активы"],
        "риски_возможности": ["риск", "возможность", "угроза", "потенциал"],
        "priority_keywords": ["приоритет", "выбор"] # Used in _analyze_strategic_thinking for bonus
    }
}
EMPATHETIC_MARKERS = {
    "en": {
        "perspective": ["viewpoint", "position", "through someone's eyes"],
        "feelings": ["feelings", "emotions", "experiences", "sensations"],
        "motivation": ["motivation", "needs", "desires", "why"],
        "understanding": ["understand", "see", "realize", "imagine"],
        "pronouns": ["we", "they", "their"], # Used in _analyze_empathetic_thinking for bonus
        "people_refs": ["people", "clients", "users"] # Used in _analyze_empathetic_thinking for bonus
    },
    "ru": {
        "перспектива": ["точка зрения", "позиция", "глазами кого-то"],
        "чувства": ["чувства", "эмоции", "переживания", "ощущения"],
        "мотивация": ["мотивация", "потребности", "желания", "почему"],
        "понимание": ["понять", "увидеть", "осознать", "представить"],
        "pronouns": ["мы", "они", "их"], # Used in _analyze_empathetic_thinking for bonus
        "people_refs": ["люди", "клиенты", "пользователи"] # Used in _analyze_empathetic_thinking for bonus
    }
}
ABSTRACT_MARKERS = {
    "en": {
        "concepts": ["concept", "idea", "principle", "theory", "model"],
        "generalization": ["generalization", "abstraction", "general", "universal"],
        "classification": ["classification", "category", "type", "kind"],
        "symbols": ["symbol", "sign", "representation"],
        "specific_examples_negators": ["for example", "specifically"] # Used in _analyze_abstract_thinking for bonus
    },
    "ru": {
        "концепции": ["концепция", "идея", "принцип", "теория", "модель"],
        "обобщение": ["обобщение", "абстракция", "общий", "универсальный"],
        "классификация": ["классификация", "категория", "тип", "вид"],
        "символы": ["символ", "знак", "представление"],
        "specific_examples_negators": ["например", "конкретно"] # Used in _analyze_abstract_thinking for bonus
    }
}
PRACTICAL_MARKERS = {
    "en": {
        "action": ["action", "implementation", "application", "do", "execute"],
        "result": ["result", "effect", "benefit", "advantage", "achievement"],
        "resources": ["resources", "budget", "time", "tools", "materials"],
        "constraints": ["constraint", "obstacle", "difficulty", "opportunity"],
        "action_verbs": ["create", "develop", "implement", "optimize", "improve"] # Used in _analyze_practical_thinking for bonus
    },
    "ru": {
        "действие": ["действие", "реализация", "применение", "сделать", "выполнить"],
        "результат": ["результат", "эффект", "польза", "выгода", "достижение"],
        "ресурсы": ["ресурсы", "бюджет", "время", "инструменты", "материалы"],
        "ограничения": ["ограничение", "препятствие", "сложность", "возможность"],
        "action_verbs": ["создать", "разработать", "внедрить", "оптимизировать", "улучшить"] # Used in _analyze_practical_thinking for bonus
    }
}
INTEGRATIVE_MARKERS = {
    "en": {
        "synthesis": [
            "integration", "synthesis", "combination", "fusion",
            "holistic", "unified", "merger"
        ],
        "diversity": [
            "different viewpoints", "different approaches", "multifaceted",
            "diversity", "includes"
        ],
        "balance": [
            "balance", "harmony", "compromise", "coordination",
            "optimal combination"
        ],
        "bonus_keywords": ["win-win", "synergy"] # Used in _analyze_integrative_thinking for bonus
    },
    "ru": {
        "синтез": [
            "интеграция", "синтез", "объединение", "комбинация",
            "целостный", "единый", "слияние"
        ],
        "разнообразие": [
            "различные точки зрения", "разные подходы", "многосторонний",
            "разнообразие", "включает в себя"
        ],
        "баланс": [
            "баланс", "гармония", "компромисс", "согласование",
            "оптимальное сочетание"
        ],
        "bonus_keywords": ["win-win", "синергия"] # Used in _analyze_integrative_thinking for bonus
    }
}
EVOLUTIONARY_MARKERS = {
    "en": {
        "development": ["development", "evolution", "progress", "growth", "change"],
        "adaptation": ["adaptation", "adjustment", "flexibility", "response to changes"],
        "iteration": ["iteration", "repetition", "cycle", "gradually", "phases"],
        "feedback": ["feedback", "lessons", "experience", "correction"],
        "bonus_keywords": ["learning", "improvement"] # Used in _analyze_evolutionary_thinking for bonus
    },
    "ru": {
        "развитие": ["развитие", "эволюция", "прогресс", "рост", "изменение"],
        "адаптация": ["адаптация", "приспособление", "гибкость", "реакция на изменения"],
        "итерация": ["итерация", "повторение", "цикл", "постепенно", "фазы"],
        "обратная_связь": ["обратная связь", "уроки", "опыт", "корректировка"],
        "bonus_keywords": ["обучение", "улучшение"] # Used in _analyze_evolutionary_thinking for bonus
    }
}
CONVERGENT_MARKERS = {
    "en": {
        "choice": ["choice", "decision", "optimal", "best", "single"],
        "criteria": ["criteria", "evaluation", "comparison", "analysis", "filter"],
        "narrowing": ["narrowing", "focus", "specific", "particular"],
        "conclusion": ["conclusion", "inference", "summary", "result"],
        "logical_connectors_leading_to_conclusion": ["thus", "therefore", "consequently"] # Used in _analyze_convergent_thinking for bonus
    },
    "ru": {
        "выбор": ["выбор", "решение", "оптимальный", "лучший", "единственный"],
        "критерии": ["критерии", "оценка", "сравнение", "анализ", "фильтр"],
        "сужение": ["сужение", "фокус", "конкретный", "специфический"],
        "заключение": ["заключение", "вывод", "итог", "результат"],
        "logical_connectors_leading_to_conclusion": ["таким образом", "следовательно", "поэтому"] # Used in _analyze_convergent_thinking for bonus
    }
}
DIVERGENT_MARKERS = {
    "en": {
        "generation": ["generation", "idea", "option", "alternative", "suggestion"],
        "expansion": ["expansion", "multitude", "variety", "more", "new"],
        "brainstorming": ["brainstorming", "creativity", "unconventional", "creative"],
        "exploration": ["exploration", "study", "search", "discovery"],
        "question_phrases": ["how else can", "what if"] # Used in _analyze_divergent_thinking for bonus
    },
    "ru": {
        "генерация": ["генерация", "идея", "вариант", "альтернатива", "предложение"],
        "расширение": ["расширение", "множество", "разнообразие", "больше", "новые"],
        "мозговой_штурм": ["мозговой штурм", "креативность", "нестандартный", "творческий"],
        "исследование": ["исследование", "изучение", "поиск", "открытие"],
        "question_phrases": ["как еще можно", "что если"] # Used in _analyze_divergent_thinking for bonus
    }
}
REFLECTIVE_MARKERS = {
    "en": {
        "self_analysis": ["reflection", "self-analysis", "contemplation", "my experience", "I think"],
        "lessons": ["lesson", "conclusion", "experience", "extract", "learn"],
        "process": ["thinking process", "how I thought", "my approach", "strategy"],
        "reassessment": ["reassessment", "re-evaluation", "adjustment", "change of mind"],
        "bonus_keywords": ["future improvement", "reapplication"] # Used in _analyze_reflective_thinking for bonus
    },
    "ru": {
        "самоанализ": ["рефлексия", "самоанализ", "осмысление", "мой опыт", "я думаю"],
        "уроки": ["урок", "вывод", "опыт", "извлечь", "научиться"],
        "процесс": ["процесс мышления", "как я думал", "мой подход", "стратегия"],
        "переоценка": ["переоценка", "переосмысление", "корректировка", "изменение мнения"],
        "bonus_keywords": ["будущего улучшения", "повторного применения"] # Used in _analyze_reflective_thinking for bonus
    }
}

EMOTIONAL_WORDS = {
    "en": {
        "positive": ["good", "excellent", "great", "success", "joy", "happy", "positive", "optimistic"],
        "negative": ["bad", "terrible", "failure", "sadness", "problem", "unhappy", "negative", "pessimistic"]
    },
    "ru": {
        "positive": ["хорошо", "отлично", "прекрасно", "успех", "радость", "счастлив", "позитивно", "оптимистично"],
        "negative": ["плохо", "ужасно", "провал", "грусть", "проблема", "несчастлив", "негативно", "пессимистично"]
    }
}

AMBIGUITY_MARKERS = {
    "en": ["unclear", "undefined", "may be", "possibly", "if", "or", "ambiguous", "vague"],
    "ru": ["неясно", "неопределенно", "может быть", "возможно", "если", "или", "неоднозначно", "смутно"]
}

DOMAIN_KEYWORDS = {
    "en": {
        "programming": ["code", "program", "algorithm", "software", "development", "bug", "feature"],
        "business": ["marketing", "sales", "client", "revenue", "profit", "strategy", "market"],
        "science": ["science", "research", "data", "experiment", "theory", "hypothesis", "analysis"],
        "general": ["general"] # Fallback domain
    },
    "ru": {
        "programming": ["код", "программа", "алгоритм", "разработка", "баг", "фича"],
        "business": ["маркетинг", "продажи", "клиент", "доход", "прибыль", "стратегия", "рынок"],
        "science": ["наука", "исследование", "данные", "эксперимент", "теория", "гипотеза", "анализ"],
        "general": ["общее"] # Fallback domain
    }
}

TYPE_STYLES = {
    "en": {
        "observation": ("🔍", "OBSERVATION"),
        "hypothesis": ("💡", "HYPOTHESIS"),
        "analysis": ("🔬", "ANALYSIS"),
        "synthesis": ("🔄", "SYNTHESIS"),
        "evaluation": ("⚖️", "EVALUATION"),
        "conclusion": ("🎯", "CONCLUSION"),
        "question": ("❓", "QUESTION"),
        "assumption": ("🤔", "ASSUMPTION"),
        "counterargument": ("⚡", "COUNTERARGUMENT"),
        "metacognition": ("🧠", "METACOGNITION"),
        "default": ("💭", "THOUGHT") # Fallback for unknown type
    },
    "ru": {
        "observation": ("🔍", "НАБЛЮДЕНИЕ"),
        "hypothesis": ("💡", "ГИПОТЕЗА"),
        "analysis": ("🔬", "АНАЛИЗ"),
        "synthesis": ("🔄", "СИНТЕЗ"),
        "evaluation": ("⚖️", "ОЦЕНКА"),
        "conclusion": ("🎯", "ЗАКЛЮЧЕНИЕ"),
        "question": ("❓", "ВОПРОС"),
        "assumption": ("🤔", "ДОПУЩЕНИЕ"),
        "counterargument": ("⚡", "КОНТРАРГУМЕНТ"),
        "metacognition": ("🧠", "МЕТАКОГНИЦИЯ"),
        "default": ("💭", "МЫСЛЬ") # Fallback for unknown type
    }
}

STRATEGY_DESCRIPTIONS = {
    "en": {
        "linear": "Sequential linear thinking: step by step",
        "tree": "Tree-like exploration of alternatives: branching and merging",
        "dialectical": "Dialectical thinking: thesis-antithesis-synthesis",
        "systematic": "Systematic analysis: by components",
        "creative": "Creative non-linear thinking: finding new ideas",
        "analytical": "Strictly logical analysis: deduction and induction",
        "metacognitive": "Thinking about thinking: self-analysis of the process",
        "critical": "Critical thinking: evaluating information reliability and arguments",
        "systemic": "Systemic thinking: analyzing holistic systems and their interconnections",
        "lateral": "Lateral thinking: seeking non-obvious solutions and unconventional approaches",
        "strategic": "Strategic thinking: analyzing long-term consequences and planning",
        "empathetic": "Empathetic thinking: considering viewpoints and feelings of others",
        "abstract": "Abstract thinking: working with models, theories, and generalizations",
        "practical": "Practical thinking: focusing on feasibility and concrete results",
        "integrative": "Integrative thinking: synthesizing different viewpoints and approaches",
        "evolutionary": "Evolutionary thinking: iterative development and adaptation",
        "convergent": "Convergent thinking: finding the optimal solution and narrowing options",
        "divergent": "Divergent thinking: generating multiple alternatives and ideas",
        "reflective": "Reflective thinking: self-analysis of the thinking process and extracting lessons"
    },
    "ru": {
        "linear": "Последовательное линейное мышление: шаг за шагом",
        "tree": "Древовидное исследование альтернатив: ветвление и слияние",
        "dialectical": "Диалектическое мышление: тезис-антитезис-синтез",
        "systematic": "Систематический анализ: по компонентам",
        "creative": "Креативное нелинейное мышление: поиск новых идей",
        "analytical": "Строго логический анализ: дедукция и индукция",
        "metacognitive": "Мышление о мышлении: самоанализ процесса",
        "critical": "Критическое мышление: оценка достоверности информации и аргументов",
        "systemic": "Системное мышление: анализ целостных систем и их взаимосвязей",
        "lateral": "Латеральное мышление: поиск неочевидных решений и нестандартных подходов",
        "strategic": "Стратегическое мышление: анализ долгосрочных последствий и планирование",
        "empathetic": "Эмпатическое мышление: рассмотрение точек зрения и чувств других",
        "abstract": "Абстрактное мышление: работа с моделями, теориями и обобщениями",
        "practical": "Практическое мышление: фокус на реализуемости и конкретных результатах",
        "integrative": "Интегративное мышление: синтез разных точек зрения и подходов",
        "evolutionary": "Эволюционное мышление: итеративное развитие и адаптация",
        "convergent": "Конвергентное мышление: поиск оптимального решения и сужение вариантов",
        "divergent": "Дивергентное мышление: генерация множества альтернатив и идей",
        "reflective": "Рефлексивное мышление: самоанализ процесса мышления и извлечение уроков"
    }
}