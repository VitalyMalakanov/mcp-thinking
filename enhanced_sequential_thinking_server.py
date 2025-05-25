# enhanced_sequential_thinking_server.py

"""
Enhanced MCP Server: Advanced Tool for LLM Sequential Thinking

Description:
This enhanced MCP server provides advanced tools for structured LLM thinking,
including reasoning chains, tree-like thought structures, metacognitive processes,
logical consistency checking, and adaptive planning.

All translations and language-specific markers are stored exclusively in:
- `localization.py` for user messages, headers, errors, help texts, etc.
- `localization_markers.py` for thinking strategy markers and analysis patterns.
The main script only imports and uses functions and dictionaries from these files,
without duplicating any localized strings or markers.

Key Enhancements:
- Tree-like thought structure with branching and merging support
- Metacognitive analysis of reasoning quality
- Logical consistency checking between thoughts
- Adaptive planning with strategy adjustment
- Confidence and thought quality assessment system
- Cognitive bias detection
- Automatic contradiction identification
- Support for various thinking strategies

Installation of dependencies:
pip install 'fastmcp' colorama numpy scikit-learn textstat sentence-transformers

Run:
python enhanced_sequential_thinking_server.py
"""

import sys
import logging
import json
import re
import math
from typing import Optional, List, Dict, Any, Union, Tuple, Set
from collections import defaultdict, deque
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
import asyncio

# Localization imports
from localization import t, DEFAULT_LANG, TRANSLATIONS
from localization_markers import (
    COGNITIVE_BIAS_MARKERS, CONTRADICTION_WORDS, LOGICAL_CONNECTORS,
    EVIDENCE_PATTERNS, UNCERTAINTY_MARKERS, CERTAINTY_MARKERS,
    CRITICAL_MARKERS, SYSTEMIC_MARKERS, LATERAL_MARKERS, STRATEGIC_MARKERS,
    EMPATHETIC_MARKERS, ABSTRACT_MARKERS, PRACTICAL_MARKERS, INTEGRATIVE_MARKERS,
    EVOLUTIONARY_MARKERS, CONVERGENT_MARKERS, DIVERGENT_MARKERS, REFLECTIVE_MARKERS,
    TYPE_STYLES, STRATEGY_DESCRIPTIONS, DOMAIN_KEYWORDS, EMOTIONAL_WORDS, AMBIGUITY_MARKERS
)

# For text analysis and semantic similarity
try:
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import textstat
    HAS_ANALYSIS_LIBS = True
except ImportError:
    print(t("WARNING_ANALYSIS_LIBS_NOT_FOUND", lang=DEFAULT_LANG))
    HAS_ANALYSIS_LIBS = False

# For colored console output
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print(t("WARNING_COLORAMA_NOT_FOUND", lang=DEFAULT_LANG))
    class Fore:
        RED = YELLOW = GREEN = BLUE = CYAN = MAGENTA = ''
    class Style:
        RESET_ALL = BRIGHT = DIM = ''

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('thinking_server.log')
    ]
)
logger = logging.getLogger(__name__)

# Add filter for important messages
class ImportantFilter(logging.Filter):
    def filter(self, record):
        return (
            record.levelno >= logging.WARNING or
            "initialization" in record.getMessage() or
            "called" in record.getMessage() # This log is now localized via t()
        )

logger.addFilter(ImportantFilter())


# Import MCP components - CRITICAL CHANGE HERE
try:
    from fastmcp import FastMCP # <-- CHANGED IMPORT PATH
    import mcp.types as types # Still need mcp.types
    from mcp.server.session import ServerSession # Still need mcp.server.session for patching, if it's there
    from pydantic import BaseModel, Field, ValidationError
    from fastapi import Request 
    logger.info(t("INFO_MCP_SDK_IMPORTED", lang=DEFAULT_LANG))
except ImportError as e:
    print(f"{t('ERROR_MCP_SDK_IMPORT_FAILED', lang=DEFAULT_LANG)}: {e}")
    sys.exit(1)

# Initialize FastMCP instance globally before class definitions
mcp_instance = FastMCP("enhanced-sequential-thinking-server")

# Apply patch for ServerSession (similar to original)
# NOTE: This patch might become unnecessary or need adjustment with FastMCP 2.0+
# as the underlying library behavior might have changed.
if 'ServerSession' in globals() and ServerSession is not None:
    try:
        old__received_request = ServerSession._received_request
        async def _received_request(self, *args, **kwargs):
            try:
                return await old__received_request(self, *args, **kwargs)
            except RuntimeError as e:
                logger.debug(t("WARNING_PATCH_RUNTIME_ERROR_CAUGHT", lang=DEFAULT_LANG), exc_info=e)
                pass
        ServerSession._received_request = _received_request
        logger.info(t("INFO_PATCH_APPLIED", lang=DEFAULT_LANG))
    except Exception as e:
        logger.error(t("ERROR_PATCH_APPLY_FAILED", lang=DEFAULT_LANG), exc_info=e)

# ============================================================================
# DATA MODELS AND ENUMS
# ============================================================================

class ThinkingStrategy(Enum):
    """Thinking Strategies"""
    LINEAR = "linear"
    TREE = "tree"
    DIALECTICAL = "dialectical"
    SYSTEMATIC = "systematic"
    CREATIVE = "creative"
    ANALYTICAL = "analytical"
    METACOGNITIVE = "metacognitive"
    CRITICAL = "critical"
    SYSTEMIC = "systemic"
    LATERAL = "lateral"
    STRATEGIC = "strategic"
    EMPATHETIC = "empathetic"
    ABSTRACT = "abstract"
    PRACTICAL = "practical"
    INTEGRATIVE = "integrative"
    EVOLUTIONARY = "evolutionary"
    CONVERGENT = "convergent"
    DIVERGENT = "divergent"
    REFLECTIVE = "reflective"

class ThoughtType(Enum):
    """Types of Thoughts"""
    OBSERVATION = "observation"
    HYPOTHESIS = "hypothesis"
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"
    EVALUATION = "evaluation"
    CONCLUSION = "conclusion"
    QUESTION = "question"
    ASSUMPTION = "assumption"
    COUNTERARGUMENT = "counterargument"
    METACOGNITION = "metacognition"

class ConfidenceLevel(Enum):
    """Confidence Levels"""
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5

@dataclass
class ThoughtMetrics:
    """Metrics for Thought Quality"""
    clarity_score: float = 0.0
    logical_coherence: float = 0.0
    evidence_strength: float = 0.0
    novelty_score: float = 0.0
    complexity_score: float = 0.0
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEDIUM
    critical_thinking_score: float = 0.0
    systemic_thinking_score: float = 0.0
    lateral_thinking_score: float = 0.0
    strategic_score: float = 0.0
    empathy_score: float = 0.0
    abstraction_score: float = 0.0
    practicality_score: float = 0.0
    integration_score: float = 0.0
    evolution_score: float = 0.0
    convergence_score: float = 0.0
    divergence_score: float = 0.0
    reflection_score: float = 0.0

@dataclass
class EnhancedThought:
    """Enhanced Thought Structure"""
    id: str
    content: str
    thought_type: ThoughtType
    strategy: ThinkingStrategy
    parent_id: Optional[str] = None
    children_ids: List[str] = field(default_factory=list)
    branch_id: Optional[str] = None
    revision_of: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    metrics: ThoughtMetrics = field(default_factory=ThoughtMetrics)
    cognitive_biases: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    supports: List[str] = field(default_factory=list)
    contradicts: List[str] = field(default_factory=list)
    builds_on: List[str] = field(default_factory=list)

class EnhancedThinkingInput(BaseModel):
    """Input data for the enhanced thinking tool"""
    thought: str = Field(description="Content of the thought")
    thought_type: ThoughtType = Field(default=ThoughtType.ANALYSIS, description="Type of thought")
    strategy: ThinkingStrategy = Field(default=ThinkingStrategy.LINEAR, description="Thinking strategy")
    parent_thought_id: Optional[str] = Field(None, description="ID of the parent thought")
    revision_of_id: Optional[str] = Field(None, description="ID of the thought being revised")
    branch_id: Optional[str] = Field(None, description="Identifier of the branch")
    supports_thoughts: List[str] = Field(default_factory=list, description="IDs of thoughts being supported")
    contradicts_thoughts: List[str] = Field(default_factory=list, description="IDs of thoughts being contradicted")
    builds_on_thoughts: List[str] = Field(default_factory=list, description="IDs of thoughts being built upon")
    tags: List[str] = Field(default_factory=list, description="Tags for categorization")
    confidence: Optional[ConfidenceLevel] = Field(None, description="Confidence level")
    response_language: Optional[str] = Field(None, description="Requested language for the response output (e.g., 'en', 'ru')")
    request_analysis: bool = Field(default=True, description="Request quality analysis")
    request_validation: bool = Field(default=True, description="Request validation")

class MetacognitionInput(BaseModel):
    """Input data for metacognitive analysis"""
    focus_area: str = Field(description="Area for metacognitive analysis")
    thinking_session_id: Optional[str] = Field(None, description="ID of the thinking session")
    analysis_depth: int = Field(default=3, ge=1, le=5, description="Depth of analysis (1-5)")

class StrategyAdaptationInput(BaseModel):
    """Input data for strategy adaptation"""
    current_strategy: ThinkingStrategy = Field(description="Current strategy")
    effectiveness_score: float = Field(ge=0.0, le=1.0, description="Effectiveness score (0-1)")
    context: str = Field(description="Task context")
    constraints: List[str] = Field(default_factory=list, description="Constraints")


# ============================================================================
# MAIN THINKING PROCESSOR
# ============================================================================

class CognitiveValidation:
    """Validation of Cognitive Processes"""

    def __init__(self, language: str = DEFAULT_LANG):
        self.language = language

    def set_language(self, lang: str):
        self.language = lang

    def detect_cognitive_biases(self, thought: str) -> List[str]:
        """Improved detection of cognitive biases"""
        biases = COGNITIVE_BIAS_MARKERS[self.language]
        detected_biases = []
        thought_lower = thought.lower()
        for bias_name, bias_data in biases.items():
            marker_count = sum(1 for marker in bias_data["markers"] if marker in thought_lower)
            context_matches = any(context in thought_lower for context in bias_data["context"])
            if marker_count >= 2 and context_matches:
                detected_biases.append(bias_name)
        return detected_biases

    def check_logical_consistency(self, thoughts: List[str]) -> Dict[str, Any]:
        """Check logical consistency between thoughts"""
        if not HAS_ANALYSIS_LIBS or len(thoughts) < 2:
            return {"consistent": True, "conflicts": [], "similarity_matrix": []}
        try:
            vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
            vectors = vectorizer.fit_transform(thoughts)
            similarity_matrix = cosine_similarity(vectors).tolist()
            conflicts = []
            contradiction_words_set = CONTRADICTION_WORDS[self.language]
            for i, thought1 in enumerate(thoughts):
                for j, thought2 in enumerate(thoughts[i+1:], i+1):
                    for neg, pos in contradiction_words_set:
                        if neg in thought1.lower() and pos in thought2.lower():
                            if similarity_matrix[i][j] < 0.3:
                                conflicts.append({
                                    "thoughts": [i, j],
                                    "type": t("semantic_contradiction", lang=self.language),
                                    "confidence": 1.0 - similarity_matrix[i][j]
                                })
            return {
                "consistent": len(conflicts) == 0,
                "conflicts": conflicts,
                "similarity_matrix": similarity_matrix
            }
        except Exception as e:
            logger.error(t("ERROR_LOGICAL_CONSISTENCY_CHECK_FAILED", lang=self.language), exc_info=e)
            return {"consistent": True, "conflicts": [], "similarity_matrix": []}

class ThoughtQualityAnalyzer:
    """Thought Quality Analyzer"""

    def __init__(self, language: str = DEFAULT_LANG):
        self.language = language

    def set_language(self, lang: str):
        self.language = lang

    def analyze_thought_quality(self, thought: str, strategy: ThinkingStrategy = ThinkingStrategy.LINEAR) -> ThoughtMetrics:
        """Comprehensive analysis of thought quality considering thinking strategy"""
        metrics = ThoughtMetrics()
        if not thought.strip():
            return metrics

        if HAS_ANALYSIS_LIBS:
            try:
                flesch_score = textstat.flesch_reading_ease(thought)
                metrics.clarity_score = min(1.0, max(0.0, flesch_score / 100.0))
                word_count = len(thought.split())
                sentence_count = len([s for s in re.split(r'[.!?]+', thought) if s.strip()])
                avg_sentence_length = word_count / max(sentence_count, 1)
                metrics.complexity_score = min(1.0, avg_sentence_length / 20.0)
            except Exception:
                word_count = len(thought.split())
                metrics.clarity_score = min(1.0, max(0.1, 1.0 - (word_count - 10) / 100.0))
                metrics.complexity_score = min(1.0, word_count / 50.0)
        else:
            word_count = len(thought.split())
            metrics.clarity_score = min(1.0, max(0.1, 1.0 - abs(word_count - 15) / 30.0))
            metrics.complexity_score = min(1.0, word_count / 50.0)

        if strategy == ThinkingStrategy.CRITICAL: metrics.critical_thinking_score = self._analyze_critical_thinking(thought)
        elif strategy == ThinkingStrategy.SYSTEMIC: metrics.systemic_thinking_score = self._analyze_systemic_thinking(thought)
        elif strategy == ThinkingStrategy.LATERAL: metrics.lateral_thinking_score = self._analyze_lateral_thinking(thought)
        elif strategy == ThinkingStrategy.STRATEGIC: metrics.strategic_score = self._analyze_strategic_thinking(thought)
        elif strategy == ThinkingStrategy.EMPATHETIC: metrics.empathy_score = self._analyze_empathetic_thinking(thought)
        elif strategy == ThinkingStrategy.ABSTRACT: metrics.abstraction_score = self._analyze_abstract_thinking(thought)
        elif strategy == ThinkingStrategy.PRACTICAL: metrics.practicality_score = self._analyze_practical_thinking(thought)
        elif strategy == ThinkingStrategy.INTEGRATIVE: metrics.integration_score = self._analyze_integrative_thinking(thought)
        elif strategy == ThinkingStrategy.EVOLUTIONARY: metrics.evolution_score = self._analyze_evolutionary_thinking(thought)
        elif strategy == ThinkingStrategy.CONVERGENT: metrics.convergence_score = self._analyze_convergent_thinking(thought)
        elif strategy == ThinkingStrategy.DIVERGENT: metrics.divergence_score = self._analyze_divergent_thinking(thought)
        elif strategy == ThinkingStrategy.REFLECTIVE: metrics.reflection_score = self._analyze_reflective_thinking(thought)

        logical_connectors_set = LOGICAL_CONNECTORS[self.language]
        connector_count = sum(1 for conn in logical_connectors_set if conn in thought.lower())
        metrics.logical_coherence = min(1.0, connector_count / 3.0)

        evidence_patterns_set = EVIDENCE_PATTERNS[self.language]
        evidence_count = sum(1 for pattern in evidence_patterns_set if re.search(pattern, thought.lower()))
        metrics.evidence_strength = min(1.0, evidence_count / 3.0)

        unique_words = len(set(thought.lower().split()))
        total_words = len(thought.split())
        if total_words > 0:
            lexical_diversity = unique_words / total_words
            metrics.novelty_score = min(1.0, lexical_diversity)

        uncertainty_markers_set = UNCERTAINTY_MARKERS[self.language]
        certainty_markers_set = CERTAINTY_MARKERS[self.language]
        uncertainty_count = sum(1 for marker in uncertainty_markers_set if marker in thought.lower())
        certainty_count = sum(1 for marker in certainty_markers_set if marker in thought.lower())

        if certainty_count > uncertainty_count: metrics.confidence_level = ConfidenceLevel.HIGH
        elif uncertainty_count > certainty_count: metrics.confidence_level = ConfidenceLevel.LOW
        else: metrics.confidence_level = ConfidenceLevel.MEDIUM
        return metrics

    def _analyze_specific_strategy(self, thought: str, markers_data: Dict[str, List[str]], bonus_structure_keywords: Optional[List[Tuple[str,str]]] = None, bonus_causal_keywords: Optional[List[str]] = None, bonus_question_phrases: Optional[List[str]] = None, bonus_priority_keywords: Optional[List[str]] = None, bonus_people_refs: Optional[Dict[str,List[str]]] = None, bonus_specific_examples_negators: Optional[List[str]] = None, bonus_action_verbs: Optional[List[str]] = None, bonus_keywords: Optional[List[str]]=None, bonus_logical_connectors_conclusion: Optional[List[str]]=None ) -> float:
        """Generic helper for analyzing thinking strategies based on markers."""
        scores = []
        thought_lower = thought.lower()
        word_count = len(thought.split())
        if word_count == 0: return 0.0

        for category, markers in markers_data.items():
            if category.endswith("_keywords") or category.endswith("_phrases") or category.endswith("_negators") or category.endswith("_verbs") or category == "pronouns" or category == "people_refs": # Skip special bonus keywords
                continue
            count = sum(1 for marker in markers if marker in thought_lower)
            normalized_score = min(1.0, count / (word_count * 0.1))
            scores.append(normalized_score)
        
        bonus_score = 0.0
        if bonus_structure_keywords and any((m1 in thought_lower and m2 in thought_lower) for m1, m2 in bonus_structure_keywords): bonus_score = 0.2
        if bonus_causal_keywords and any(keyword in thought_lower for keyword in bonus_causal_keywords): bonus_score = 0.1
        if bonus_question_phrases and any(q_word in thought_lower for q_word in bonus_question_phrases): bonus_score = 0.15
        if bonus_priority_keywords and any(keyword in thought_lower for keyword in bonus_priority_keywords): bonus_score = 0.1
        if bonus_people_refs and any(p_word in thought_lower for p_word in bonus_people_refs["pronouns"]) and any(ref_word in thought_lower for ref_word in bonus_people_refs["people_refs"]): bonus_score = 0.1
        if bonus_specific_examples_negators and not any(num.isdigit() for num in thought) and not any(word in thought_lower for word in bonus_specific_examples_negators): bonus_score = 0.1
        if bonus_action_verbs and any(verb in thought_lower for verb in bonus_action_verbs): bonus_score = 0.1
        if bonus_keywords and any(keyword in thought_lower for keyword in bonus_keywords): bonus_score = 0.15 if "win-win" in bonus_keywords or "synergy" in bonus_keywords else 0.1
        if bonus_logical_connectors_conclusion and any(conn in thought_lower for conn in bonus_logical_connectors_conclusion): bonus_score = 0.1
        
        if bonus_score > 0: scores.append(bonus_score)
        return sum(scores) / len(scores) if scores else 0.0

    def _analyze_critical_thinking(self, thought: str) -> float:
        markers_data = CRITICAL_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_structure_keywords=markers_data.get("structure_keywords"))
    def _analyze_systemic_thinking(self, thought: str) -> float:
        markers_data = SYSTEMIC_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_causal_keywords=markers_data.get("causal_keywords"))
    def _analyze_lateral_thinking(self, thought: str) -> float:
        markers_data = LATERAL_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_question_phrases=markers_data.get("question_phrases"))
    def _analyze_strategic_thinking(self, thought: str) -> float:
        markers_data = STRATEGIC_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_priority_keywords=markers_data.get("priority_keywords"))
    def _analyze_empathetic_thinking(self, thought: str) -> float:
        markers_data = EMPATHETIC_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_people_refs={"pronouns": markers_data.get("pronouns",[]), "people_refs": markers_data.get("people_refs",[])})
    def _analyze_abstract_thinking(self, thought: str) -> float:
        markers_data = ABSTRACT_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_specific_examples_negators=markers_data.get("specific_examples_negators"))
    def _analyze_practical_thinking(self, thought: str) -> float:
        markers_data = PRACTICAL_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_action_verbs=markers_data.get("action_verbs"))
    def _analyze_integrative_thinking(self, thought: str) -> float:
        markers_data = INTEGRATIVE_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_keywords=markers_data.get("bonus_keywords"))
    def _analyze_evolutionary_thinking(self, thought: str) -> float:
        markers_data = EVOLUTIONARY_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_keywords=markers_data.get("bonus_keywords"))
    def _analyze_convergent_thinking(self, thought: str) -> float:
        markers_data = CONVERGENT_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_logical_connectors_conclusion=markers_data.get("logical_connectors_leading_to_conclusion"))
    def _analyze_divergent_thinking(self, thought: str) -> float:
        markers_data = DIVERGENT_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_question_phrases=markers_data.get("question_phrases"))
    def _analyze_reflective_thinking(self, thought: str) -> float:
        markers_data = REFLECTIVE_MARKERS[self.language]
        return self._analyze_specific_strategy(thought, markers_data, bonus_keywords=markers_data.get("bonus_keywords"))


class EnhancedThinkingProcessor:
    """Advanced Processor for Thoughts"""

    def __init__(self, language: str = DEFAULT_LANG):
        self.language = language
        self.thoughts: Dict[str, EnhancedThought] = {}
        self.thought_sessions: Dict[str, List[str]] = defaultdict(list)
        self.current_session_id: str = "default"
        self.strategy_history: List[Tuple[ThinkingStrategy, float]] = [] # Will store (strategy, effectiveness) tuples
        self.global_thought_counter: int = 0
        self.quality_analyzer = ThoughtQualityAnalyzer(language=self.language)
        self.cognitive_validator = CognitiveValidation(language=self.language)

    def set_language(self, lang: str):
        self.language = lang
        self.quality_analyzer.set_language(lang)
        self.cognitive_validator.set_language(lang)

    def generate_thought_id(self) -> str:
        """Generates a unique thought ID"""
        self.global_thought_counter += 1
        return f"thought_{self.global_thought_counter}_{datetime.now().strftime('%H%M%S')}"

    def create_thought(self, input_data: EnhancedThinkingInput) -> EnhancedThought:
        """Creates a new thought with full analysis"""
        thought_id = self.generate_thought_id()

        thought = EnhancedThought(
            id=thought_id,
            content=input_data.thought,
            thought_type=input_data.thought_type,
            strategy=input_data.strategy,
            parent_id=input_data.parent_thought_id,
            branch_id=input_data.branch_id,
            revision_of=input_data.revision_of_id,
            supports=input_data.supports_thoughts,
            contradicts=input_data.contradicts_thoughts,
            builds_on=input_data.builds_on_thoughts,
            tags=input_data.tags
        )

        if input_data.request_analysis:
            thought.metrics = self.quality_analyzer.analyze_thought_quality(
                input_data.thought,
                input_data.strategy
            )
            if input_data.confidence:
                thought.metrics.confidence_level = input_data.confidence

        if input_data.request_validation:
            thought.cognitive_biases = self.cognitive_validator.detect_cognitive_biases(input_data.thought)

        self._update_thought_relationships(thought)
        self.thoughts[thought_id] = thought
        self.thought_sessions[self.current_session_id].append(thought_id)
        return thought

    def _update_thought_relationships(self, thought: EnhancedThought):
        """Updates relationships between thoughts"""
        if thought.parent_id and thought.parent_id in self.thoughts:
            parent = self.thoughts[thought.parent_id]
            if thought.id not in parent.children_ids:
                parent.children_ids.append(thought.id)

    def get_thinking_path(self, thought_id: str) -> List[EnhancedThought]:
        """Retrieves the thinking path up to the specified thought"""
        if thought_id not in self.thoughts:
            return []
        path = []
        current_thought = self.thoughts[thought_id]
        while current_thought:
            path.insert(0, current_thought)
            if current_thought.parent_id:
                current_thought = self.thoughts.get(current_thought.parent_id)
            else:
                break
        return path

    def analyze_session_coherence(self, session_id: str = None) -> Dict[str, Any]:
        """Analyzes the coherence of a thinking session"""
        if session_id is None:
            session_id = self.current_session_id
        if session_id not in self.thought_sessions:
            return {"error": t("ERROR_SESSION_NOT_FOUND", lang=self.language)}
        thought_ids = self.thought_sessions[session_id]
        thoughts_content = [self.thoughts[tid].content for tid in thought_ids if tid in self.thoughts]
        if not thoughts_content:
            return {"coherence_score": 0.0, "analysis": t("ANALYSIS_NO_THOUGHTS", lang=self.language)}
        
        consistency_analysis = self.cognitive_validator.check_logical_consistency(thoughts_content)
        quality_scores = []
        for tid in thought_ids:
            if tid in self.thoughts:
                thought = self.thoughts[tid]
                avg_quality = (
                    thought.metrics.clarity_score +
                    thought.metrics.logical_coherence +
                    thought.metrics.evidence_strength
                ) / 3.0
                quality_scores.append(avg_quality)
        quality_trend = 0.0
        if len(quality_scores) > 1:
            quality_trend = quality_scores[-1] - quality_scores[0]
        return {
            "coherence_score": 1.0 - len(consistency_analysis["conflicts"]) / max(len(thoughts_content), 1),
            "consistency_analysis": consistency_analysis,
            "quality_trend": quality_trend,
            "average_quality": sum(quality_scores) / len(quality_scores) if quality_scores else 0.0,
            "thought_count": len(thoughts_content),
            "cognitive_biases_detected": sum(len(self.thoughts[tid].cognitive_biases)
                                           for tid in thought_ids if tid in self.thoughts)
        }

    def suggest_next_thinking_strategy(self, context: str, current_effectiveness: float, current_strategy: ThinkingStrategy) -> Dict[str, Any]:
        """Improved recommendations for thinking strategies, including recording current strategy effectiveness"""
        # Record current strategy effectiveness
        self.strategy_history.append((current_strategy, current_effectiveness))
        if len(self.strategy_history) > 20: # Keep a limited history
            self.strategy_history.pop(0)

        context_analysis = {
            "complexity": self._analyze_complexity(context),
            "ambiguity": self._analyze_ambiguity(context),
            "emotional_tone": self._analyze_emotional_tone(context),
            "domain": self._detect_domain(context)
        }
        
        analyzed_strategy_history = self._analyze_strategy_history()
        recommendations = []
        
        if context_analysis["complexity"] > 0.7: recommendations.extend([(ThinkingStrategy.SYSTEMIC, t("HIGH_COMPLEXITY_REASON", lang=self.language)), (ThinkingStrategy.ANALYTICAL, t("DETAILED_ANALYSIS_NEEDED_REASON", lang=self.language))])
        if context_analysis["ambiguity"] > 0.6: recommendations.extend([(ThinkingStrategy.CRITICAL, t("AMBIGUITY_CRITICAL_ANALYSIS_REASON", lang=self.language)), (ThinkingStrategy.DIALECTICAL, t("OPPOSING_VIEWPOINTS_REASON", lang=self.language))])
        if context_analysis["emotional_tone"] > 0.5: recommendations.extend([(ThinkingStrategy.EMPATHETIC, t("EMOTIONAL_CONTEXT_EMPATHETIC_REASON", lang=self.language)), (ThinkingStrategy.REFLECTIVE, t("REFLECTION_NEEDED_REASON", lang=self.language))])
        
        if analyzed_strategy_history:
            successful_strategies = [strat for strat, eff in analyzed_strategy_history if eff > 0.7]
            if successful_strategies: recommendations.extend([(strat, t("STRATEGY_EFFECTIVE_PREVIOUSLY_REASON", lang=self.language)) for strat in successful_strategies[:2]])
        
        if not recommendations:
            if current_effectiveness < 0.5: recommendations.extend([(ThinkingStrategy.TREE, t("EXPLORE_ALTERNATIVES_REASON", lang=self.language)), (ThinkingStrategy.DIALECTICAL, t("OPPOSING_VIEWPOINTS_REASON", lang=self.language)), (ThinkingStrategy.METACOGNITIVE, t("ANALYZE_APPROACH_REASON", lang=self.language))])
            elif current_effectiveness < 0.7: recommendations.extend([(ThinkingStrategy.SYSTEMATIC, t("USE_SYSTEMATIC_ANALYSIS_REASON", lang=self.language)), (ThinkingStrategy.ANALYTICAL, t("APPLY_STRICT_LOGIC_REASON", lang=self.language))])
            else: recommendations.extend([(ThinkingStrategy.CREATIVE, t("TRY_CREATIVE_APPROACH_REASON", lang=self.language)), (ThinkingStrategy.DIVERGENT, t("GENERATE_MORE_ALTERNATIVES_REASON", lang=self.language))])

        return {
            "context_analysis": context_analysis,
            "current_effectiveness": current_effectiveness,
            "suggested_strategies": recommendations,
            "reasoning": t("RECOMMENDATION_REASONING_SUFFIX", lang=self.language)
        }

    def _analyze_complexity(self, text: str) -> float:
        """Analyzes text complexity (simple heuristic)."""
        if not text.strip(): return 0.0
        word_count = len(text.split())
        long_word_count = sum(1 for word in text.split() if len(word) > 7)
        sentence_count = len(re.split(r'[.!?]+', text))
        if sentence_count == 0: return 0.0
        complexity = (long_word_count / word_count) * (word_count / sentence_count) if word_count > 0 else 0.0
        return min(1.0, complexity / 5.0)

    def _analyze_ambiguity(self, text: str) -> float:
        """Analyzes text ambiguity (simple heuristic)."""
        ambiguity_markers_set = AMBIGUITY_MARKERS[self.language]
        count = sum(1 for marker in ambiguity_markers_set if marker in text.lower())
        word_count = len(text.split())
        return min(1.0, count / (word_count * 0.1) if word_count > 0 else 0.0)

    def _analyze_emotional_tone(self, text: str) -> float:
        """Analyzes emotional tone (very simple heuristic)."""
        positive_words = EMOTIONAL_WORDS[self.language]["positive"]
        negative_words = EMOTIONAL_WORDS[self.language]["negative"]
        text_lower = text.lower()
        positive_score = sum(1 for word in positive_words if word in text_lower)
        negative_score = sum(1 for word in negative_words if word in text_lower)
        total_score = positive_score + negative_score
        if total_score == 0: return 0.0
        return abs(positive_score - negative_score) / total_score

    def _detect_domain(self, text: str) -> str:
        """Detects domain (very simple heuristic)."""
        text_lower = text.lower()
        for domain, keywords in DOMAIN_KEYWORDS[self.language].items():
            if any(keyword in text_lower for keyword in keywords):
                return t(f"TEXT_DOMAIN_{domain.upper()}", lang=self.language)
        return t("TEXT_DOMAIN_GENERAL", lang=self.language)

    def _analyze_strategy_history(self) -> List[Tuple[ThinkingStrategy, float]]:
        """Analyzes strategy effectiveness history."""
        return self.strategy_history[-5:] # Return last 5 entries, now populated

    def perform_metacognitive_analysis(self, focus_area: str, depth: int = 3) -> Dict[str, Any]:
        """Metacognitive analysis of the thinking process."""
        session_thoughts = [self.thoughts[tid] for tid in self.thought_sessions[self.current_session_id] if tid in self.thoughts]
        if not session_thoughts:
            return {"analysis": t("ANALYSIS_NO_THOUGHTS", lang=self.language), "recommendations": []}
        analysis = {
            "focus_area": focus_area,
            "thinking_patterns": self._analyze_thinking_patterns(session_thoughts),
            "strategy_effectiveness": self._evaluate_strategy_effectiveness(session_thoughts),
            "cognitive_load": self._assess_cognitive_load(session_thoughts),
            "bias_assessment": self._assess_cognitive_biases(session_thoughts),
            "recommendations": []
        }
        recommendations = []
        if analysis["cognitive_load"] > 0.7: recommendations.append(t("RECOMMENDATION_BREAK_DOWN_TASK", lang=self.language))
        if len(analysis["bias_assessment"]["detected_biases"]) > 3: recommendations.append(t("RECOMMENDATION_BIASES_ATTENTION", lang=self.language))
        if analysis["strategy_effectiveness"] < 0.5: recommendations.append(t("RECOMMENDATION_STRATEGY_INEFFECTIVE", lang=self.language))
        analysis["recommendations"] = recommendations
        return analysis

    def _analyze_thinking_patterns(self, thoughts: List[EnhancedThought]) -> Dict[str, Any]:
        """Analyzes thinking patterns."""
        if not thoughts: return {}
        type_distribution = defaultdict(int)
        strategy_distribution = defaultdict(int)
        for thought in thoughts:
            type_distribution[thought.thought_type.value] += 1
            strategy_distribution[thought.strategy.value] += 1
        return {
            "thought_type_distribution": dict(type_distribution),
            "strategy_distribution": dict(strategy_distribution),
            "dominant_type": max(type_distribution.items(), key=lambda x: x[1])[0] if type_distribution else None,
            "dominant_strategy": max(strategy_distribution.items(), key=lambda x: x[1])[0] if strategy_distribution else None
        }

    def _evaluate_strategy_effectiveness(self, thoughts: List[EnhancedThought]) -> float:
        """Evaluates strategy effectiveness based on average quality of thoughts produced with it."""
        # This is a simple proxy. Real effectiveness would depend on task success.
        if not thoughts: return 0.0
        total_quality = 0.0
        for thought in thoughts:
            quality = (thought.metrics.clarity_score + thought.metrics.logical_coherence + thought.metrics.evidence_strength + thought.metrics.novelty_score) / 4.0
            total_quality += quality
        return total_quality / len(thoughts) if thoughts else 0.0

    def _assess_cognitive_load(self, thoughts: List[EnhancedThought]) -> float:
        """Assesses cognitive load based on thought complexity and interconnections."""
        if not thoughts: return 0.0
        total_complexity = sum(thought.metrics.complexity_score for thought in thoughts)
        avg_complexity = total_complexity / len(thoughts) if thoughts else 0.0
        connection_complexity = 0.0
        for thought in thoughts:
            connections = len(thought.supports) + len(thought.contradicts) + len(thought.builds_on)
            connection_complexity += connections / 10.0
        avg_connection_complexity = connection_complexity / len(thoughts) if thoughts else 0.0
        return min(1.0, (avg_complexity + avg_connection_complexity) / 2.0)

    def _assess_cognitive_biases(self, thoughts: List[EnhancedThought]) -> Dict[str, Any]:
        """Assesses cognitive biases across a list of thoughts."""
        all_biases = []
        bias_distribution_map = defaultdict(int)
        for thought in thoughts:
            all_biases.extend(thought.cognitive_biases)
            for bias in thought.cognitive_biases:
                bias_distribution_map[bias] += 1
        return {
            "total_biases": len(all_biases),
            "unique_biases": len(set(all_biases)),
            "detected_biases": list(set(all_biases)),
            "bias_distribution": dict(bias_distribution_map),
            "bias_density": len(all_biases) / len(thoughts) if thoughts else 0.0
        }

# ============================================================================
# OUTPUT FORMATTERS
# ============================================================================

class EnhancedOutputFormatter:
    """Formatter for pretty output of results."""

    def __init__(self, language: str = DEFAULT_LANG):
        self.language = language

    def set_language(self, lang: str):
        self.language = lang

    def format_thought_display(self, thought: EnhancedThought) -> str:
        """Formatted output of a thought with analysis."""
        type_styles_data = TYPE_STYLES[self.language]
        icon, type_name_key = type_styles_data.get(thought.thought_type.value, type_styles_data["default"])
        type_name = t(type_name_key, lang=self.language) 

        fore_color_map = {
            ThoughtType.OBSERVATION: Fore.BLUE, ThoughtType.HYPOTHESIS: Fore.YELLOW,
            ThoughtType.ANALYSIS: Fore.GREEN, ThoughtType.SYNTHESIS: Fore.MAGENTA,
            ThoughtType.EVALUATION: Fore.CYAN, ThoughtType.CONCLUSION: Fore.RED,
            ThoughtType.QUESTION: Fore.YELLOW, ThoughtType.ASSUMPTION: Fore.BLUE,
            ThoughtType.COUNTERARGUMENT: Fore.RED, ThoughtType.METACOGNITION: Fore.MAGENTA
        }
        fore_color = fore_color_map.get(thought.thought_type, Fore.WHITE)

        header_parts = [f"{fore_color}{icon} {type_name}{Style.RESET_ALL}", f"{t('THOUGHT_HEADER_ID', lang=self.language)}: {thought.id[-8:]}..."]
        if thought.branch_id: header_parts.append(f"{t('THOUGHT_HEADER_BRANCH', lang=self.language)}: {thought.branch_id}")
        if thought.revision_of: header_parts.append(f"🔄 {t('THOUGHT_HEADER_REVISES', lang=self.language)}: {thought.revision_of[-8:]}...")
        header = " | ".join(header_parts)

        metrics = thought.metrics
        quality_bar = self._create_quality_bar(metrics)

        strategy_score = 0.0
        # Simplified way to get strategy score if available
        strategy_score_attr_map = {
            ThinkingStrategy.CRITICAL: "critical_thinking_score", ThinkingStrategy.SYSTEMIC: "systemic_thinking_score",
            ThinkingStrategy.LATERAL: "lateral_thinking_score", ThinkingStrategy.STRATEGIC: "strategic_score",
            ThinkingStrategy.EMPATHETIC: "empathy_score", ThinkingStrategy.ABSTRACT: "abstraction_score",
            ThinkingStrategy.PRACTICAL: "practicality_score", ThinkingStrategy.INTEGRATIVE: "integration_score",
            ThinkingStrategy.EVOLUTIONARY: "evolution_score", ThinkingStrategy.CONVERGENT: "convergence_score",
            ThinkingStrategy.DIVERGENT: "divergence_score", ThinkingStrategy.REFLECTIVE: "reflection_score",
        }
        score_attr_name = strategy_score_attr_map.get(thought.strategy)
        if score_attr_name and hasattr(metrics, score_attr_name):
            strategy_score = getattr(metrics, score_attr_name)
        strategy_metric = f"{t('Strategy Score', lang=self.language)}: {strategy_score:.2f}"
        
        connections = []
        if thought.supports: connections.append(f"✅ {t('Supports', lang=self.language)}: {len(thought.supports)}")
        if thought.contradicts: connections.append(f"⚡ {t('Contradicts', lang=self.language)}: {len(thought.contradicts)}")
        if thought.builds_on: connections.append(f"🏗️ {t('Builds on', lang=self.language)}: {len(thought.builds_on)}")
        connections_str = " | ".join(connections) if connections else t("No connections", lang=self.language)

        biases_str = ", ".join(thought.cognitive_biases) if thought.cognitive_biases else t("None detected", lang=self.language)
        tags_str = " #" + " #".join(thought.tags) if thought.tags else t("No tags", lang=self.language)
        strategy_description = STRATEGY_DESCRIPTIONS[self.language].get(thought.strategy.value, t("DESCRIPTION_UNAVAILABLE", lang=self.language))

        content_lines = [
            header,
            f"{t('Strategy', lang=self.language)}: {thought.strategy.value}",
            f"{t('Strategy Description', lang=self.language)}: {strategy_description}",
            quality_bar,
            strategy_metric,
            f"{t('Connections', lang=self.language)}: {connections_str}",
            f"{t('Biases', lang=self.language)}: {biases_str}",
            f"{t('Tags', lang=self.language)}:{tags_str}",
            "",
            thought.content
        ]
        max_width = max(len(line) for line in content_lines) + 4
        border = "─" * max_width
        result_lines = [f"┌{border}┐", f"│ {header:<{max_width-2}} │"]
        for line in content_lines[1:]:
            result_lines.append(f"├{border}┤" if line == "" else f"│ {line:<{max_width-2}} │")
        result_lines.append(f"└{border}┘")
        return "\n".join(result_lines)

    def _create_quality_bar(self, metrics: ThoughtMetrics) -> str:
        """Creates a visual quality bar."""
        def make_bar(value: float, length: int = 10) -> str:
            filled = int(value * length)
            return "█" * filled + "░" * (length - filled)
        bars = [
            f"{t('Clarity', lang=self.language)}: {make_bar(metrics.clarity_score)} {metrics.clarity_score:.2f}",
            f"{t('Logic', lang=self.language)}: {make_bar(metrics.logical_coherence)} {metrics.logical_coherence:.2f}",
            f"{t('Evidence', lang=self.language)}: {make_bar(metrics.evidence_strength)} {metrics.evidence_strength:.2f}",
            f"{t('Novelty', lang=self.language)}: {make_bar(metrics.novelty_score)} {metrics.novelty_score:.2f}",
            f"{t('Confidence', lang=self.language)}: {metrics.confidence_level.name}"
        ]
        return " | ".join(bars)

    def format_session_analysis(self, analysis: Dict[str, Any]) -> str:
        """Formats session analysis."""
        lines = [
            f"\n{Fore.CYAN}{t('SESSION ANALYSIS', lang=self.language)}{Style.RESET_ALL}", "=" * 50,
            f"{t('Coherence Score', lang=self.language)}: {analysis.get('coherence_score', 0):.2f}",
            f"{t('Quality Trend', lang=self.language)}: {analysis.get('quality_trend', 0):+.2f}",
            f"{t('Average Quality', lang=self.language)}: {analysis.get('average_quality', 0):.2f}",
            f"{t('Thought Count', lang=self.language)}: {analysis.get('thought_count', 0)}",
            f"{t('Cognitive Biases', lang=self.language)}: {analysis.get('cognitive_biases_detected', 0)}"
        ]
        if analysis.get('consistency_analysis', {}).get('conflicts'):
            lines.append(f"\n{t('LOGICAL CONFLICTS_DETECTED', lang=self.language)}")
            for i, conflict in enumerate(analysis['consistency_analysis']['conflicts'][:3]):
                lines.append(f"  {i+1}. {conflict.get('type', t('UNKNOWN_CONFLICT_TYPE', lang=self.language))} ({t('Confidence', lang=self.language)}: {conflict.get('confidence', 0):.2f})")
        return "\n".join(lines)

    def format_metacognitive_analysis(self, analysis: Dict[str, Any]) -> str:
        """Formats metacognitive analysis."""
        lines = [
            f"\n{Fore.MAGENTA}{t('METACOGNITIVE ANALYSIS', lang=self.language)}{Style.RESET_ALL}", "=" * 50,
            f"{t('Focus Area', lang=self.language)}: {analysis.get('focus_area', t('GENERAL_FOCUS_AREA', lang=self.language))}",
        ]
        patterns = analysis.get('thinking_patterns', {})
        if patterns.get('dominant_type'): lines.append(f"{t('Dominant Thought Type', lang=self.language)}: {patterns['dominant_type']}")
        if patterns.get('dominant_strategy'): lines.append(f"{t('Dominant Strategy', lang=self.language)}: {patterns['dominant_strategy']}")
        lines.extend([
            f"{t('Strategy Effectiveness', lang=self.language)}: {analysis.get('strategy_effectiveness', 0):.2f}",
            f"{t('Cognitive Load', lang=self.language)}: {analysis.get('cognitive_load', 0):.2f}"
        ])
        recommendations = analysis.get('recommendations', [])
        if recommendations:
            lines.append(f"\n{Fore.GREEN}{t('RECOMMENDATIONS', lang=self.language)}{Style.RESET_ALL}")
            for i, rec in enumerate(recommendations, 1): lines.append(f"  {i}. {rec}")
        return "\n".join(lines)

# ============================================================================
# MCP SERVER AND TOOLS
# ============================================================================

class EnhancedThinkingServer:
    """Server for processing thoughts with asynchronous initialization and MCP tools."""
    def __init__(self, language: str = DEFAULT_LANG):
        self.language = language
        self._initialized = False
        self._init_lock = asyncio.Lock()
        self._init_event = asyncio.Event()
        
        self.thinking_processor = EnhancedThinkingProcessor(language=self.language)
        self.output_formatter = EnhancedOutputFormatter(language=self.language)

    def set_language(self, lang: str):
        self.language = lang
        self.thinking_processor.set_language(lang)
        self.output_formatter.set_language(lang)

    async def initialize(self):
        """Asynchronous server initialization."""
        async with self._init_lock:
            if not self._initialized:
                try:
                    if not all([hasattr(self, attr) for attr in ['thinking_processor', 'output_formatter']]):
                        raise RuntimeError(t("ERROR_COMPONENTS_NOT_INIT", lang=self.language))
                    await self._validate_components()
                    self._initialized = True
                    self._init_event.set()
                    logger.info(t("INFO_SERVER_INIT_COMPLETED", lang=self.language))
                except Exception as e:
                    logger.error(t("ERROR_INIT_FAILED", lang=self.language), exc_info=e)
                    self._initialized = False
                    raise

    async def _validate_components(self):
        """Checks component operability."""
        try:
            test_input = EnhancedThinkingInput(thought="Test thought for validation", thought_type=ThoughtType.OBSERVATION, strategy=ThinkingStrategy.ANALYTICAL)
            test_thought = EnhancedThought(id="val_id", content=test_input.thought, thought_type=test_input.thought_type, strategy=test_input.strategy)
            test_thought.metrics = self.thinking_processor.quality_analyzer.analyze_thought_quality(test_input.thought, test_input.strategy)
            test_thought.cognitive_biases = self.thinking_processor.cognitive_validator.detect_cognitive_biases(test_input.thought)
            self.output_formatter.format_thought_display(test_thought)
            logger.info(t("INFO_COMPONENT_VALIDATION_SUCCESS", lang=self.language))
        except Exception as e:
            logger.error(t("ERROR_COMPONENT_VALIDATION_FAILED", lang=self.language), exc_info=e)
            raise

    async def ensure_initialized(self):
        """Ensures server is initialized, waiting if necessary."""
        if not self._initialized:
            logger.info(t("INFO_WAITING_INIT", lang=self.language))
            try:
                await asyncio.wait_for(self._init_event.wait(), timeout=10.0) 
                logger.info(t("INFO_SERVER_INIT_DONE", lang=self.language))
            except asyncio.TimeoutError:
                logger.error(t("ERROR_INIT_TIMEOUT", lang=self.language))
                raise RuntimeError(t("ERROR_INIT_TIMEOUT", lang=self.language))
            except Exception as e:
                logger.error(t("ERROR_INIT_WAIT_ERROR", lang=self.language), exc_info=e)
                raise

    @mcp_instance.tool()
    async def enhanced_thinking(self, input: EnhancedThinkingInput) -> List[types.TextContent]:
        """
        Advanced tool for processing sequential thoughts with quality analysis,
        cognitive bias detection, and support for various thinking strategies.

        Args:
            input: Extended thought data with meta-information
        """
        original_formatter_language = server.output_formatter.language
        try:
            await server.ensure_initialized()
            if not input.thought or len(input.thought.strip()) == 0:
                raise ValueError(t("ERROR_EMPTY_THOUGHT_CONTENT", lang=server.language))
            
            current_response_language = input.response_language if input.response_language and input.response_language in TRANSLATIONS else server.language
            server.output_formatter.set_language(current_response_language)
                
            logger.info(f"{t('INFO_CALL_LOG_GENERIC', lang=server.language)}: {t('TOOL_NAME_ENHANCED_THINKING', lang=server.language)} - {input.thought[:50]}...")
            thought = server.thinking_processor.create_thought(input)
            if not thought or not thought.id:
                raise RuntimeError(t("ERROR_FAILED_TO_CREATE_THOUGHT", lang=server.language))
                
            formatted_output = server.output_formatter.format_thought_display(thought)
            print(formatted_output, file=sys.stderr)
            
            return [types.TextContent(type="text", text=json.dumps({
                "thought_id": thought.id,
                "analysis": {
                    "quality_metrics": {k: v for k, v in thought.metrics.__dict__.items() if not k.startswith('_') and not isinstance(v, Enum)} | {"confidence_level": thought.metrics.confidence_level.name},
                    "cognitive_biases": thought.cognitive_biases,
                    "connections": {"supports": thought.supports, "contradicts": thought.contradicts, "builds_on": thought.builds_on, "children": thought.children_ids}
                },
                "metadata": {"thought_type": thought.thought_type.value, "strategy": thought.strategy.value, "timestamp": thought.timestamp.isoformat(), "tags": thought.tags}
            }, indent=2))]
            
        except ValueError as e:
            logger.error(f"{t('ERROR_INPUT_VALIDATION_ERROR_PREFIX', lang=server.language)} {t('TOOL_NAME_ENHANCED_THINKING', lang=server.language)}: {e}")
            error_result = {"input": {"error": str(e), "status": "failed"}}
            return [types.TextContent(type="text", text=json.dumps(error_result, indent=2))]
        except Exception as e:
            logger.exception(f"{t('ERROR_TOOL_EXECUTION_FAILED_PREFIX', lang=server.language)} {t('TOOL_NAME_ENHANCED_THINKING', lang=server.language)}")
            error_result = {"input": {"error": str(e), "status": "failed"}}
            return [types.TextContent(type="text", text=json.dumps(error_result, indent=2))]
        finally:
            server.output_formatter.set_language(original_formatter_language)


    @mcp_instance.tool()
    async def analyze_thinking_session(self, session_id: Optional[str] = None) -> List[types.TextContent]:
        original_formatter_language = server.output_formatter.language
        try:
            await server.ensure_initialized()
            server.output_formatter.set_language(server.language) 
            logger.info(f"{t('INFO_CALL_LOG_GENERIC', lang=server.language)}: {t('TOOL_NAME_ANALYZE_SESSION', lang=server.language)}: {session_id or 'current'}")
            analysis = server.thinking_processor.analyze_session_coherence(session_id)
            formatted_output = server.output_formatter.format_session_analysis(analysis)
            print(formatted_output, file=sys.stderr)
            return [types.TextContent(type="text", text=json.dumps(analysis, indent=2))]
        except Exception as e:
            logger.exception(f"{t('ERROR_TOOL_EXECUTION_FAILED_PREFIX', lang=server.language)} {t('TOOL_NAME_ANALYZE_SESSION', lang=server.language)}")
            error_result = {"input": {"error": str(e), "status": "failed"}}
            return [types.TextContent(type="text", text=json.dumps(error_result, indent=2))]
        finally:
            server.output_formatter.set_language(original_formatter_language)

    @mcp_instance.tool()
    async def metacognitive_reflection(self, input: MetacognitionInput) -> List[types.TextContent]:
        original_formatter_language = server.output_formatter.language
        try:
            await server.ensure_initialized()
            server.output_formatter.set_language(server.language)
            logger.info(f"{t('INFO_CALL_LOG_GENERIC', lang=server.language)}: {t('TOOL_NAME_METACOGNITIVE_REFLECTION', lang=server.language)}: {input.focus_area}")
            analysis = server.thinking_processor.perform_metacognitive_analysis(input.focus_area, input.analysis_depth)
            formatted_output = server.output_formatter.format_metacognitive_analysis(analysis)
            print(formatted_output, file=sys.stderr)
            return [types.TextContent(type="text", text=json.dumps(analysis, indent=2))]
        except Exception as e:
            logger.exception(f"{t('ERROR_TOOL_EXECUTION_FAILED_PREFIX', lang=server.language)} {t('TOOL_NAME_METACOGNITIVE_REFLECTION', lang=server.language)}")
            error_result = {"input": {"error": str(e), "status": "failed"}}
            return [types.TextContent(type="text", text=json.dumps(error_result, indent=2))]
        finally:
            server.output_formatter.set_language(original_formatter_language)

    @mcp_instance.tool()
    async def adapt_thinking_strategy(self, input: StrategyAdaptationInput) -> List[types.TextContent]:
        original_formatter_language = server.output_formatter.language
        try:
            await server.ensure_initialized()
            server.output_formatter.set_language(server.language)
            logger.info(f"{t('INFO_CALL_LOG_GENERIC', lang=server.language)}: {t('TOOL_NAME_ADAPT_STRATEGY', lang=server.language)}: {input.current_strategy.value} -> ?")
            suggestions = server.thinking_processor.suggest_next_thinking_strategy(input.context, input.effectiveness_score, input.current_strategy) 
            
            strategy_info = [
                f"\n{Fore.YELLOW}{t('STRATEGY_ADAPTATION_TITLE', lang=server.language)}{Style.RESET_ALL}", "=" * 40,
                f"{t('Current Strategy', lang=server.language)}: {input.current_strategy.value}",
                f"{t('Effectiveness', lang=server.language)}: {input.effectiveness_score:.2f}",
                f"{t('Context', lang=server.language)}: {input.context[:50]}...",
                f"\n{t('Suggested Strategies', lang=server.language)}"
            ]
            for strategy_enum, reason in suggestions.get('suggested_strategies', []):
                strategy_info.append(f"  • {strategy_enum.value}: {reason}")
            formatted_output = "\n".join(strategy_info)
            print(formatted_output, file=sys.stderr)

            def enum_serializer(obj):
                if isinstance(obj, Enum): return obj.value
                raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
            return [types.TextContent(type="text", text=json.dumps(suggestions, indent=2, default=enum_serializer))]
        except Exception as e:
            logger.exception(f"{t('ERROR_TOOL_EXECUTION_FAILED_PREFIX', lang=server.language)} {t('TOOL_NAME_ADAPT_STRATEGY', lang=server.language)}")
            error_result = {"input": {"error": str(e), "status": "failed"}}
            return [types.TextContent(type="text", text=json.dumps(error_result, indent=2))]
        finally:
            server.output_formatter.set_language(original_formatter_language)

    @mcp_instance.tool()
    async def get_thinking_path(self, thought_id: str) -> List[types.TextContent]:
        original_formatter_language = server.output_formatter.language
        try:
            await server.ensure_initialized()
            server.output_formatter.set_language(server.language)
            logger.info(f"{t('INFO_CALL_LOG_GENERIC', lang=server.language)}: {t('TOOL_NAME_GET_PATH', lang=server.language)}: {thought_id}")
            path = server.thinking_processor.get_thinking_path(thought_id)
            if not path:
                result = {"error": t("THOUGHT_NOT_FOUND", lang=server.language, thought_id=thought_id), "path": []}
            else:
                path_data = []
                for i, thought in enumerate(path):
                    path_data.append({
                        "step": i + 1, "thought_id": thought.id, "content": thought.content,
                        "type": thought.thought_type.value, "strategy": thought.strategy.value,
                        "quality_score": (thought.metrics.clarity_score + thought.metrics.logical_coherence + thought.metrics.evidence_strength) / 3.0
                    })
                result = {"thought_id": thought_id, "path_length": len(path), "path": path_data}
                path_lines = [f"\n{Fore.GREEN}{t('THINKING PATH', lang=server.language)}{Style.RESET_ALL}", "=" * 40]
                for step_data in path_data:
                    path_lines.append(f"{step_data['step']}. [{step_data['type']}] {step_data['content'][:60]}... ({t('QUALITY_SCORE_SHORT', lang=server.language)}: {step_data['quality_score']:.2f})")
                formatted_output = "\n".join(path_lines)
                print(formatted_output, file=sys.stderr)
            return [types.TextContent(type="text", text=json.dumps(result, indent=2))]
        except Exception as e:
            logger.exception(f"{t('ERROR_TOOL_EXECUTION_FAILED_PREFIX', lang=server.language)} {t('TOOL_NAME_GET_PATH', lang=server.language)}")
            error_result = {"input": {"error": str(e), "status": "failed"}}
            return [types.TextContent(type="text", text=json.dumps(error_result, indent=2))]
        finally:
            server.output_formatter.set_language(original_formatter_language)

    @mcp_instance.tool()
    async def export_thinking_session(self, session_id: Optional[str] = None, format_type: str = "json") -> List[types.TextContent]:
        original_formatter_language = server.output_formatter.language
        try:
            await server.ensure_initialized()
            server.output_formatter.set_language(server.language) 
            logger.info(f"{t('INFO_CALL_LOG_GENERIC', lang=server.language)}: {t('TOOL_NAME_EXPORT_SESSION', lang=server.language)}: {format_type}")
            if session_id is None: session_id = server.thinking_processor.current_session_id
            if session_id not in server.thinking_processor.thought_sessions:
                return [types.TextContent(type="text", text=json.dumps({"error": t("ERROR_SESSION_NOT_FOUND", lang=server.language)}))]
            thought_ids = server.thinking_processor.thought_sessions[session_id]
            thoughts = [server.thinking_processor.thoughts[tid] for tid in thought_ids if tid in server.thinking_processor.thoughts]

            if format_type == "json":
                export_data = {"session_id": session_id, "export_timestamp": datetime.now().isoformat(), "thought_count": len(thoughts), "thoughts": []}
                for thought in thoughts:
                    export_data["thoughts"].append({
                        "id": thought.id, "content": thought.content, "type": thought.thought_type.value, "strategy": thought.strategy.value,
                        "timestamp": thought.timestamp.isoformat(), 
                        "metrics": {k: v for k, v in thought.metrics.__dict__.items() if not k.startswith('_') and not isinstance(v, Enum)} | {"confidence_level": thought.metrics.confidence_level.name},
                        "biases": thought.cognitive_biases,
                        "connections": {"parent": thought.parent_id, "children": thought.children_ids, "supports": thought.supports, "contradicts": thought.contradicts},
                        "tags": thought.tags
                    })
            elif format_type == "markdown":
                lines = [f"# {t('EXPORT_SESSION_TITLE', lang=server.language)}", f"**{t('EXPORT_SESSION_ID', lang=server.language)}:** {session_id}", f"**{t('EXPORT_DATE', lang=server.language)}:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", f"**{t('EXPORT_TOTAL_THOUGHTS', lang=server.language)}:** {len(thoughts)}", "", f"## {t('EXPORT_THOUGHTS_HEADING', lang=server.language)}", ""]
                for i, thought in enumerate(thoughts, 1):
                    lines.extend([f"### {i}. {thought.thought_type.value.title()}", f"**{t('THOUGHT_HEADER_ID', lang=server.language)}:** {thought.id}", f"**{t('Strategy', lang=server.language)}:** {thought.strategy.value}", f"**{t('AVERAGE_QUALITY_MARKDOWN', lang=server.language)}:** {t('Clarity', lang=server.language)} {thought.metrics.clarity_score:.2f} | {t('Logic', lang=server.language)} {thought.metrics.logical_coherence:.2f} | {t('Evidence', lang=server.language)} {thought.metrics.evidence_strength:.2f}", "", thought.content, ""])
                    if thought.cognitive_biases: lines.extend([f"**{t('DETECTED_BIASES_MARKDOWN', lang=server.language)}**: {', '.join(thought.cognitive_biases)}", ""])
                export_data = "\n".join(lines)
            elif format_type == "summary":
                session_analysis = server.thinking_processor.analyze_session_coherence(session_id)
                quality_trend_val = session_analysis.get('quality_trend', 0)
                quality_trend_text = t("QUALITY_TREND_STABLE", lang=server.language)
                if quality_trend_val > 0: quality_trend_text = t("QUALITY_TREND_IMPROVING", lang=server.language)
                elif quality_trend_val < 0: quality_trend_text = t("QUALITY_TREND_DECLINING", lang=server.language)
                export_data = {
                    "session_summary": {"session_id": session_id, "total_thoughts": len(thoughts), "coherence_score": session_analysis.get("coherence_score", 0), "quality_trend": quality_trend_val, "average_quality": session_analysis.get("average_quality", 0), "cognitive_biases_detected": session_analysis.get("cognitive_biases_detected", 0)},
                    "key_insights": [t("SUMMARY_PROCESSED_THOUGHTS", lang=server.language, count=len(thoughts), score=session_analysis.get('coherence_score', 0)), t("SUMMARY_QUALITY_TREND", lang=server.language, trend=quality_trend_text), t("SUMMARY_DETECTED_BIASES", lang=server.language, count=session_analysis.get('cognitive_biases_detected', 0))]
                }
            else:
                export_data = {"error": t("EXPORT_UNSUPPORTED_FORMAT", lang=server.language, format_type=format_type)}
            result = export_data if isinstance(export_data, dict) else {"content": export_data, "format": format_type}
            return [types.TextContent(type="text", text=json.dumps(result, indent=2) if isinstance(result, dict) else result)]
        except Exception as e:
            logger.exception(f"{t('ERROR_TOOL_EXECUTION_FAILED_PREFIX', lang=server.language)} {t('TOOL_NAME_EXPORT_SESSION', lang=server.language)}")
            error_result = {"input": {"error": str(e), "status": "failed"}}
            return [types.TextContent(type="text", text=json.dumps(error_result, indent=2))]
        finally:
            server.output_formatter.set_language(original_formatter_language)

# Create server instance and processor
server = EnhancedThinkingServer(language=DEFAULT_LANG) 

# ============================================================================
# START SERVER
# ============================================================================

if __name__ == "__main__":
    import os
    import socket 

    server_lang = os.environ.get("LANG", DEFAULT_LANG).split('_')[0].lower()
    if server_lang not in TRANSLATIONS:
        server_lang = DEFAULT_LANG
    server.set_language(server_lang)

    asyncio.run(server.initialize())

    # Now FastMCP.run() should accept host and port directly, as per gofastmcp.com docs.
    # Set the host and port for Uvicorn via FastMCP's run method.
    server_host = "0.0.0.0" # Bind to all interfaces inside Docker
    server_port = int(os.environ.get("MCP_SERVER_PORT", "8000")) # Use Docker Compose specified port or 8000

    # These are for logging purposes only.
    server_address_for_log = server_host
    if server_address_for_log == "0.0.0.0":
         try:
            hostname = socket.gethostname()
            server_address_for_log = socket.gethostbyname(hostname)
         except socket.gaierror:
            server_address_for_log = "0.0.0.0" 

    server_port_for_log = server_port # Already an int from above

    logger.info(t("INFO_SERVER_STARTING", lang=server.language, name=mcp_instance.name))
    logger.info(t("INFO_AVAILABLE_TOOLS", lang=server.language))
    logger.info(f"    - {mcp_instance.name}/enhanced_thinking")
    logger.info(f"    - {mcp_instance.name}/analyze_thinking_session")
    logger.info(f"    - {mcp_instance.name}/metacognitive_reflection")
    logger.info(f"    - {mcp_instance.name}/adapt_thinking_strategy")
    logger.info(f"    - {mcp_instance.name}/get_thinking_path")
    logger.info(f"    - {mcp_instance.name}/export_thinking_session")
    logger.info(t("INFO_SERVER_LISTENING", lang=server.language, address=server_address_for_log, port=server_port_for_log))
    logger.info(t("INFO_PRESS_CTRL_C_TO_STOP", lang=server.language))

    try:
        # Pass host and port explicitly to mcp_instance.run(), as expected by FastMCP 2.0+
        mcp_instance.run(host=server_host, port=server_port, transport='sse')
    except KeyboardInterrupt:
        logger.info(t("INFO_SERVER_STOPPED_BY_USER", lang=server.language))
    except Exception as e:
        logger.exception(t("ERROR_UNEXPECTED_SERVER_ERROR", lang=server.language))
        sys.exit(1)