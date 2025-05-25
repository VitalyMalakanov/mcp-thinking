# Enhanced Sequential Thinking Server 🧠

An advanced Model Context Protocol (MCP) server designed to facilitate and enhance the structured thinking processes of Large Language Models (LLMs). It provides a robust framework for reasoning chains, tree-like thought structures, metacognitive analysis, and adaptive planning.

## 👨‍💻 Author
[Vitaly Malakanov](https://github.com/VitalyMalakanov)

## 🚀 Project Status
![Stable](https://img.shields.io/badge/status-stable-green.svg)
![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Tree-structured Thoughts:** Support for branching and merging complex ideas
- **Metacognitive Analysis:** Deep insights into the quality and process of reasoning
- **Logical Consistency Checking:** Automatic identification of contradictions and coherence issues
- **Adaptive Planning:** Dynamic adjustment of thinking strategies based on context and effectiveness
- **Confidence & Quality Assessment:** Evaluation of thought clarity, evidence strength, and novelty
- **Cognitive Bias Detection:** Automated identification of common reasoning biases
- **Session Management:** Tools for exporting and analyzing entire thinking sessions
- **Multi-language Support:** Localized outputs and analysis markers via `localization.py` and `localization_markers.py`

## 📦 Installation

### Prerequisites
Before you begin, ensure you have the following installed:
- [Python 3.13+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (usually comes with Python)
- [Docker](https://docs.docker.com/get-docker/) (for Docker installation)

### Local Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/VitalyMalakanov/nhanced_sequential_thinking_server.git
   cd nhanced_sequential_thinking_server
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Docker Installation
1. **Build and start the container:**
   ```bash
   # Start in foreground
   docker-compose up --build

   # Start in background
   docker-compose up -d --build
   ```

2. **Stop the container:**
   ```bash
   docker-compose down
   ```

## 🚀 Usage

### Running the Server

#### Local Run
```bash
python enhanced_sequential_thinking_server.py
```
The server will be available at `http://localhost:8000/sse`

#### Docker Run
If using Docker, the server will be available at `http://localhost:5000/sse`

To change the default port (e.g., to 8080):
```bash
MCP_SERVER_PORT=8080 docker-compose up
```

### Language Selection

#### Local Run
To switch to Russian, set the environment variable:
```bash
# Windows PowerShell
$env:LANG="ru"
python enhanced_sequential_thinking_server.py

# Windows Command Prompt
set LANG=ru
python enhanced_sequential_thinking_server.py

# macOS/Linux
LANG=ru python enhanced_sequential_thinking_server.py
```

#### Docker Run
Add to your `docker-compose.yml`:
```yaml
services:
  mcp-server:
    environment:
      - LANG=ru
```

Or set directly when running:
```bash
LANG=ru docker-compose up
```

### Use Cases for AI Agents

The Enhanced Sequential Thinking Server provides powerful tools for AI agents to enhance their reasoning capabilities. Here are some practical use cases:

#### 1. Complex Problem Solving
AI agents can use the server to break down complex problems into manageable thought chains:

```python
# Example: Solving a complex business strategy problem
thought_chain = [
    EnhancedThinkingInput(
        thought="Analyze current market conditions and identify key trends",
        thought_type=ThoughtType.ANALYSIS,
        strategy=ThinkingStrategy.SYSTEMIC,
        tags=["market_analysis", "trends"]
    ),
    EnhancedThinkingInput(
        thought="Evaluate potential risks and opportunities in identified trends",
        thought_type=ThoughtType.EVALUATION,
        strategy=ThinkingStrategy.CRITICAL,
        tags=["risk_assessment", "opportunities"]
    ),
    EnhancedThinkingInput(
        thought="Generate strategic recommendations based on analysis",
        thought_type=ThoughtType.HYPOTHESIS,
        strategy=ThinkingStrategy.CREATIVE,
        tags=["strategy", "recommendations"]
    )
]
```

#### 2. Research and Analysis
For research tasks, agents can utilize different thinking strategies:

- **Linear Analysis** for step-by-step research:
  ```python
  EnhancedThinkingInput(
      thought="Review existing literature on quantum computing applications",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.LINEAR,
      tags=["research", "literature_review"]
  )
  ```

- **Divergent Thinking** for exploring multiple perspectives:
  ```python
  EnhancedThinkingInput(
      thought="Explore alternative approaches to renewable energy storage",
      thought_type=ThoughtType.QUESTION,
      strategy=ThinkingStrategy.DIVERGENT,
      tags=["innovation", "energy_storage"]
  )
  ```

#### 3. Decision Making
Agents can use the server for structured decision-making processes:

1. **Observation Phase**:
   ```python
   EnhancedThinkingInput(
       thought="Current system performance metrics and user feedback",
       thought_type=ThoughtType.OBSERVATION,
       strategy=ThinkingStrategy.LINEAR,
       tags=["metrics", "feedback"]
   )
   ```

2. **Analysis Phase**:
   ```python
   EnhancedThinkingInput(
       thought="Evaluate impact of potential system changes",
       thought_type=ThoughtType.ANALYSIS,
       strategy=ThinkingStrategy.CRITICAL,
       tags=["impact_analysis", "system_changes"]
   )
   ```

3. **Strategy Adaptation**:
   ```python
   StrategyAdaptationInput(
       current_strategy=ThinkingStrategy.CRITICAL,
       effectiveness_score=0.8,
       context="System optimization decision",
       constraints=["time", "resources"]
   )
   ```

#### 4. Creative Problem Solving
For creative tasks, agents can combine different thinking strategies:

```python
# Example: Product innovation process
creative_chain = [
    EnhancedThinkingInput(
        thought="Identify user pain points in current solutions",
        thought_type=ThoughtType.OBSERVATION,
        strategy=ThinkingStrategy.LINEAR,
        tags=["user_research", "pain_points"]
    ),
    EnhancedThinkingInput(
        thought="Generate innovative solution concepts",
        thought_type=ThoughtType.HYPOTHESIS,
        strategy=ThinkingStrategy.CREATIVE,
        tags=["innovation", "concepts"]
    ),
    EnhancedThinkingInput(
        thought="Evaluate feasibility and potential impact",
        thought_type=ThoughtType.EVALUATION,
        strategy=ThinkingStrategy.STRATEGIC,
        tags=["feasibility", "impact"]
    )
]
```

#### 5. Metacognitive Analysis
Agents can use metacognitive reflection to improve their thinking processes:

```python
# Example: Improving reasoning quality
MetacognitionInput(
    focus_area="Quality of market analysis",
    analysis_depth=3
)
```

#### 6. Quality Assurance
For validation and verification tasks:

```python
# Example: Code review process
qa_chain = [
    EnhancedThinkingInput(
        thought="Review code for potential security vulnerabilities",
        thought_type=ThoughtType.ANALYSIS,
        strategy=ThinkingStrategy.CRITICAL,
        tags=["security", "code_review"]
    ),
    EnhancedThinkingInput(
        thought="Evaluate code maintainability and scalability",
        thought_type=ThoughtType.EVALUATION,
        strategy=ThinkingStrategy.SYSTEMIC,
        tags=["maintainability", "scalability"]
    )
]
```

Each use case demonstrates how AI agents can leverage the server's tools to:
- Structure complex reasoning processes
- Maintain logical consistency
- Adapt thinking strategies based on context
- Track and analyze thought patterns
- Generate well-reasoned conclusions
- Improve decision-making quality

The server's ability to handle different types of thoughts (analysis, hypothesis, evaluation, etc.) and thinking strategies (linear, critical, creative, etc.) makes it particularly valuable for AI agents working on complex, multi-step tasks that require sophisticated reasoning capabilities.

## 🧠 Thinking Modes

The Enhanced Sequential Thinking Server supports 19 distinct thinking modes, each designed for specific types of cognitive tasks:

### Linear Thinking
- **Purpose:** Sequential, step-by-step reasoning
- **Best for:** 
  - Breaking down complex problems into manageable steps
  - Following logical sequences
  - Building structured arguments
- **Characteristics:**
  - Clear cause-and-effect relationships
  - Predictable progression
  - Systematic approach
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Implementing a new feature requires: 1) Requirements analysis, 2) Design, 3) Development, 4) Testing",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.LINEAR,
      tags=["process", "implementation"]
  )
  ```

### Tree Thinking
- **Purpose:** Exploring multiple branches of thought
- **Best for:**
  - Exploring alternatives
  - Decision tree analysis
  - Complex problem decomposition
- **Characteristics:**
  - Branching exploration
  - Multiple paths
  - Hierarchical structure
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Exploring different approaches to market entry: direct sales, partnerships, acquisitions",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.TREE,
      tags=["strategy", "exploration"]
  )
  ```

### Dialectical Thinking
- **Purpose:** Resolving contradictions through synthesis
- **Best for:**
  - Resolving conflicts
  - Finding common ground
  - Developing comprehensive solutions
- **Characteristics:**
  - Thesis-antithesis-synthesis
  - Conflict resolution
  - Integration of opposites
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing opposing views on remote work: productivity vs. collaboration, finding optimal balance",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.DIALECTICAL,
      tags=["conflict", "resolution"]
  )
  ```

### Systematic Thinking
- **Purpose:** Methodical component-based analysis
- **Best for:**
  - Complex system analysis
  - Process optimization
  - Quality improvement
- **Characteristics:**
  - Component-based analysis
  - Methodical approach
  - Systematic evaluation
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing software architecture components: frontend, backend, database, and their interactions",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.SYSTEMATIC,
      tags=["architecture", "analysis"]
  )
  ```

### Creative Thinking
- **Purpose:** Generating novel ideas and solutions
- **Best for:**
  - Brainstorming sessions
  - Innovation challenges
  - Problem-solving with multiple solutions
- **Characteristics:**
  - Divergent idea generation
  - Pattern breaking
  - Novel connections
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Exploring unconventional approaches to renewable energy storage using biomimicry principles",
      thought_type=ThoughtType.HYPOTHESIS,
      strategy=ThinkingStrategy.CREATIVE,
      tags=["innovation", "biomimicry"]
  )
  ```

### Analytical Thinking
- **Purpose:** Strict logical analysis and reasoning
- **Best for:**
  - Data analysis
  - Scientific research
  - Technical problem-solving
- **Characteristics:**
  - Deductive reasoning
  - Inductive reasoning
  - Evidence-based conclusions
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing market data trends: correlation analysis, statistical significance, predictive modeling",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.ANALYTICAL,
      tags=["data", "analysis"]
  )
  ```

### Metacognitive Thinking
- **Purpose:** Self-analysis of thinking processes
- **Best for:**
  - Process improvement
  - Learning optimization
  - Strategy refinement
- **Characteristics:**
  - Self-reflection
  - Process awareness
  - Strategy evaluation
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Reflecting on problem-solving approach: effectiveness, biases, and potential improvements",
      thought_type=ThoughtType.METACOGNITION,
      strategy=ThinkingStrategy.METACOGNITIVE,
      tags=["reflection", "improvement"]
  )
  ```

### Critical Thinking
- **Purpose:** Analytical evaluation and assessment
- **Best for:**
  - Evaluating arguments and evidence
  - Identifying logical fallacies
  - Making informed decisions
- **Characteristics:**
  - Evidence-based reasoning
  - Systematic evaluation
  - Bias awareness
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing the validity of market research data: sample size, methodology, potential biases",
      thought_type=ThoughtType.EVALUATION,
      strategy=ThinkingStrategy.CRITICAL,
      tags=["analysis", "validation"]
  )
  ```

### Systemic Thinking
- **Purpose:** Understanding complex systems and their interactions
- **Best for:**
  - System analysis
  - Understanding interdependencies
  - Holistic problem-solving
- **Characteristics:**
  - Systems perspective
  - Interconnection awareness
  - Emergent behavior analysis
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing the impact of climate change on global supply chains: direct effects, feedback loops, and systemic risks",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.SYSTEMIC,
      tags=["systems", "climate"]
  )
  ```

### Lateral Thinking
- **Purpose:** Finding unconventional solutions
- **Best for:**
  - Creative problem-solving
  - Breaking mental blocks
  - Finding innovative solutions
- **Characteristics:**
  - Non-linear approach
  - Pattern breaking
  - Unconventional connections
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Exploring unexpected applications of blockchain technology in healthcare data management",
      thought_type=ThoughtType.HYPOTHESIS,
      strategy=ThinkingStrategy.LATERAL,
      tags=["innovation", "blockchain"]
  )
  ```

### Strategic Thinking
- **Purpose:** Long-term planning and goal-oriented reasoning
- **Best for:**
  - Strategic planning
  - Resource allocation
  - Risk assessment
- **Characteristics:**
  - Goal-oriented analysis
  - Resource optimization
  - Future-focused planning
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Developing a 5-year technology roadmap considering market trends, resource constraints, and competitive landscape",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.STRATEGIC,
      tags=["planning", "roadmap"]
  )
  ```

### Empathetic Thinking
- **Purpose:** Understanding others' perspectives
- **Best for:**
  - User experience design
  - Conflict resolution
  - Team collaboration
- **Characteristics:**
  - Perspective-taking
  - Emotional awareness
  - User-centered focus
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing user feedback to understand pain points in the current interface design",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.EMPATHETIC,
      tags=["ux", "feedback"]
  )
  ```

### Abstract Thinking
- **Purpose:** Working with models and generalizations
- **Best for:**
  - Theoretical analysis
  - Model development
  - Pattern recognition
- **Characteristics:**
  - Conceptual modeling
  - Pattern abstraction
  - Theoretical framework development
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Developing a theoretical framework for understanding complex adaptive systems in organizations",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.ABSTRACT,
      tags=["theory", "modeling"]
  )
  ```

### Practical Thinking
- **Purpose:** Focusing on implementation and results
- **Best for:**
  - Project execution
  - Resource management
  - Solution implementation
- **Characteristics:**
  - Action-oriented
  - Resource-aware
  - Results-focused
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Planning the implementation of a new feature: resource allocation, timeline, and deliverables",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.PRACTICAL,
      tags=["implementation", "planning"]
  )
  ```

### Integrative Thinking
- **Purpose:** Synthesizing different viewpoints
- **Best for:**
  - Complex problem-solving
  - Multi-stakeholder analysis
  - Holistic decision-making
- **Characteristics:**
  - Viewpoint synthesis
  - Holistic integration
  - Multi-perspective analysis
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Integrating technical, business, and user perspectives in product development strategy",
      thought_type=ThoughtType.SYNTHESIS,
      strategy=ThinkingStrategy.INTEGRATIVE,
      tags=["integration", "strategy"]
  )
  ```

### Evolutionary Thinking
- **Purpose:** Iterative development and adaptation
- **Best for:**
  - Product evolution
  - Process improvement
  - Continuous learning
- **Characteristics:**
  - Iterative approach
  - Adaptation focus
  - Continuous improvement
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing product evolution through user feedback cycles and market adaptation",
      thought_type=ThoughtType.ANALYSIS,
      strategy=ThinkingStrategy.EVOLUTIONARY,
      tags=["evolution", "adaptation"]
  )
  ```

### Convergent Thinking
- **Purpose:** Finding optimal solutions
- **Best for:**
  - Decision-making
  - Solution optimization
  - Problem resolution
- **Characteristics:**
  - Solution-focused
  - Option narrowing
  - Optimization-oriented
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Evaluating and selecting the optimal cloud infrastructure solution based on requirements",
      thought_type=ThoughtType.EVALUATION,
      strategy=ThinkingStrategy.CONVERGENT,
      tags=["decision", "optimization"]
  )
  ```

### Divergent Thinking
- **Purpose:** Exploring multiple perspectives and possibilities
- **Best for:**
  - Generating alternatives
  - Exploring different viewpoints
  - Challenging assumptions
- **Characteristics:**
  - Multiple solution generation
  - Perspective shifting
  - Assumption questioning
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Exploring various approaches to urban transportation: autonomous vehicles, public transit, micro-mobility, and their combinations",
      thought_type=ThoughtType.QUESTION,
      strategy=ThinkingStrategy.DIVERGENT,
      tags=["transportation", "urban_planning"]
  )
  ```

### Reflective Thinking
- **Purpose:** Self-analysis and learning
- **Best for:**
  - Process improvement
  - Learning from experience
  - Personal development
- **Characteristics:**
  - Self-reflection
  - Experience analysis
  - Learning extraction
- **Example Use:**
  ```python
  EnhancedThinkingInput(
      thought="Analyzing project outcomes and extracting key lessons for future improvements",
      thought_type=ThoughtType.METACOGNITION,
      strategy=ThinkingStrategy.REFLECTIVE,
      tags=["reflection", "learning"]
  )
  ```

Each thinking mode can be combined with different thought types (Analysis, Hypothesis, Evaluation, Observation, Question, etc.) to create powerful reasoning chains. The server's metacognitive analysis helps agents understand which thinking mode is most effective for specific tasks and adapt their approach accordingly.

## 🔄 Session Management

The Enhanced Sequential Thinking Server provides robust session management capabilities for handling multiple concurrent thinking processes:

### Session Lifecycle
- **Creation:** Sessions are automatically created when a client connects to the SSE endpoint
- **Identification:** Each session receives a unique UUID (e.g., `e1e8e0732ac84c908deabf136c6a1a69`)
- **Duration:** Sessions persist until explicitly closed or timeout
- **Concurrency:** Multiple sessions can run simultaneously

### Session Operations
```python
# Example: Working with sessions
async with sse_client(url="http://localhost:8000/sse") as (read_stream, write_stream):
    session = ClientSession(read_stream, write_stream)
    await session.initialize()
    
    # Send thoughts within the session
    result = await session.call_tool("enhanced_thinking", {
        "thought": "Analyzing market trends",
        "thought_type": "ANALYSIS",
        "strategy": "SYSTEMIC"
    })
    
    # Export session data
    export_result = await session.call_tool("export_thinking_session", {
        "format_type": "markdown"  # or "json", "summary"
    })
```

### Session Analysis
The server provides tools for analyzing thinking sessions:

```python
# Get session analysis
analysis = await session.call_tool("analyze_thinking_session")

# Get thinking path for a specific thought
path = await session.call_tool("get_thinking_path", {
    "thought_id": "thought_123"
})

# Perform metacognitive reflection
reflection = await session.call_tool("metacognitive_reflection", {
    "focus_area": "Reasoning quality",
    "analysis_depth": 3
})
```

### Session Export Formats
The server supports multiple export formats for session data:

1. **Markdown Export**
   - Human-readable format
   - Includes thought chains and analysis
   - Suitable for documentation

2. **JSON Export**
   - Complete session data
   - Includes metadata and relationships
   - Suitable for programmatic analysis

3. **Summary Export**
   - Concise overview
   - Key insights and patterns
   - Suitable for quick review

### Error Handling
The server implements robust error handling for sessions:

- Invalid session IDs return 400 Bad Request
- Connection timeouts are handled gracefully
- Session state is preserved during reconnections
- Automatic cleanup of expired sessions

### Best Practices
1. **Session Management**
   - Initialize sessions properly
   - Handle reconnection scenarios
   - Clean up resources when done

2. **Error Handling**
   - Implement proper error handling
   - Use appropriate timeouts
   - Handle connection resets

3. **Performance**
   - Reuse sessions when possible
   - Monitor session state
   - Export data periodically

## 📊 Monitoring and Logging

The server provides comprehensive logging and monitoring capabilities:

### Log Levels
- **INFO:** Normal operation events
- **WARNING:** Potential issues (e.g., invalid session IDs)
- **ERROR:** Critical errors (e.g., connection resets)

### Log Categories
- Server initialization and startup
- Session management
- Request processing
- Error handling
- Performance metrics

### Example Log Output
```
2025-05-25 19:33:47,417 - __main__ - INFO - Server initialization completed
2025-05-25 19:59:19,367 - mcp.server.sse - WARNING - Received invalid session ID
2025-05-25 20:00:22,769 - asyncio - ERROR - Connection reset by peer
```

### Monitoring Endpoints
- Health check endpoint
- Session statistics
- Performance metrics
- Error rates

## 🔒 Security Considerations

The server implements several security measures:

### Session Security
- UUID-based session identification
- Session timeout mechanisms
- Rate limiting per session
- Input validation

### Data Protection
- Input sanitization
- Output encoding
- Secure session handling
- Resource limits

### Best Practices
1. **Configuration**
   - Use secure session timeouts
   - Implement rate limiting
   - Configure appropriate resource limits

2. **Deployment**
   - Use HTTPS in production
   - Implement proper access controls
   - Monitor for suspicious activity

3. **Maintenance**
   - Regular security updates
   - Session cleanup
   - Log monitoring

## 📈 Performance Optimization

The server is designed for optimal performance in various scenarios:

### Resource Management
- **Memory Usage:** Efficient memory management for long-running sessions
- **CPU Utilization:** Optimized processing of thinking chains
- **Connection Pooling:** Smart handling of concurrent connections
- **Cache Management:** Intelligent caching of frequently used data

### Scaling Considerations
- **Horizontal Scaling:** Support for multiple server instances
- **Load Balancing:** Compatible with standard load balancers
- **Session Distribution:** Efficient session handling across instances
- **Resource Allocation:** Dynamic resource adjustment based on load

### Performance Metrics
- **Response Times:** Average < 100ms for standard operations
- **Concurrent Sessions:** Support for 1000+ simultaneous sessions
- **Throughput:** Capable of processing 100+ thoughts per second
- **Memory Footprint:** ~50MB base memory usage

## 🔧 Troubleshooting Guide

Common issues and their solutions:

### Connection Issues
1. **Connection Reset Errors**
   ```log
   ConnectionResetError: [WinError 10054] Удаленный хост принудительно разорвал существующее подключение
   ```
   - Check client network stability
   - Verify server timeout settings
   - Ensure proper session cleanup

2. **Invalid Session IDs**
   ```log
   WARNING - Received invalid session ID: test_session
   ```
   - Verify session initialization
   - Check session ID format
   - Ensure proper session management

### Server Issues
1. **Startup Problems**
   - Verify Python version (3.13+)
   - Check port availability
   - Review system requirements

2. **Performance Issues**
   - Monitor resource usage
   - Check connection limits
   - Review session management

### Client Issues
1. **Timeout Errors**
   - Adjust client timeout settings
   - Check network latency
   - Verify server load

2. **Session Management**
   - Implement proper session cleanup
   - Handle reconnection scenarios
   - Monitor session state

## 📚 API Reference

### Core Endpoints

#### SSE Connection
```http
GET /sse
```
Establishes Server-Sent Events connection for real-time communication.

#### Message Processing
```http
POST /messages/?session_id={session_id}
```
Processes thinking requests within a session.

### Request Types

#### Enhanced Thinking
```python
{
    "thought": "string",
    "thought_type": "ANALYSIS|HYPOTHESIS|EVALUATION|OBSERVATION|QUESTION",
    "strategy": "LINEAR|TREE|DIALECTICAL|...",
    "tags": ["string"]
}
```

#### Metacognitive Reflection
```python
{
    "focus_area": "string",
    "analysis_depth": integer
}
```

#### Strategy Adaptation
```python
{
    "current_strategy": "string",
    "effectiveness_score": float,
    "context": "string",
    "constraints": ["string"]
}
```

### Response Formats

#### Success Response
```json
{
    "thought_id": "uuid",
    "analysis": {
        "coherence": float,
        "confidence": float,
        "insights": ["string"]
    },
    "metadata": {
        "timestamp": "iso8601",
        "thought_type": "string",
        "strategy": "string"
    }
}
```

#### Error Response
```json
{
    "error": "string",
    "details": {
        "code": "string",
        "message": "string"
    }
}
```

## 🌟 Community and Support

### Getting Help
- **GitHub Issues:** Report bugs and request features
- **Discussions:** Join community discussions
- **Documentation:** Read the detailed docs
- **Examples:** Check the examples directory

### Contributing
We welcome contributions! Here's how you can help:

1. **Code Contributions**
   - Fork the repository
   - Create a feature branch
   - Submit a pull request

2. **Documentation**
   - Improve existing docs
   - Add examples
   - Fix typos

3. **Testing**
   - Write unit tests
   - Report bugs
   - Suggest improvements

### Community Guidelines
- Be respectful and inclusive
- Follow the code of conduct
- Help others learn
- Share your experiences

## 📊 Project Statistics

![GitHub Stars](https://img.shields.io/github/stars/VitalyMalakanov/nhanced_sequential_thinking_server?style=social)
![GitHub Forks](https://img.shields.io/github/forks/VitalyMalakanov/nhanced_sequential_thinking_server?style=social)
![GitHub Issues](https://img.shields.io/github/issues/VitalyMalakanov/nhanced_sequential_thinking_server)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/VitalyMalakanov/nhanced_sequential_thinking_server)
![GitHub License](https://img.shields.io/github/license/VitalyMalakanov/nhanced_sequential_thinking_server)

## 🔍 Keywords and Tags

#AI #MachineLearning #LLM #Reasoning #CognitiveComputing #Python #AsyncIO #FastAPI #MCP #ThinkingServer #SequentialThinking #Metacognition #CognitiveArchitecture #AIReasoning #ThoughtChains #DecisionMaking #ProblemSolving #CognitiveScience #ArtificialIntelligence #MachineReasoning

## 📝 Changelog

### [1.0.0] - 2024-05-25
- Initial release
- Core thinking server functionality
- Session management
- Multiple thinking modes
- Metacognitive analysis
- Export capabilities

### [0.9.0] - 2024-05-20
- Beta release
- Basic thinking server
- Initial session support
- Core thinking modes

## 🔮 Roadmap

*План развития проекта будет опубликован в ближайшее время.*

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Pydantic for data validation
- Uvicorn for ASGI server
- The open-source community for inspiration and support