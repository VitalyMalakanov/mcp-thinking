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

## 📁 Project Structure
- `enhanced_sequential_thinking_server.py` - Main server application and core thought analysis logic
- `localization.py` - Centralized translations and language support utilities
- `localization_markers.py` - Language-dependent markers and patterns for analysis
- `requirements.txt` - Python package dependencies
- `Dockerfile` - Docker image definition for the server
- `docker-compose.yml` - Docker Compose configuration for easy multi-service deployment
- `.dockerignore` - Specifies files and directories to exclude from the Docker build context
- `README.md` - This documentation file

## 🐳 Docker Configuration
The project includes Docker support for easy deployment and consistent environments:

- **Base Image:** Uses a lightweight Python 3.13 slim image
- **Port Mapping:** Default internal server port 5000 is exposed (e.g., 5000:5000 in docker-compose.yml)
- **Volume Mounts:** Allows for persistence of logs (e.g., /app/logs)
- **Environment Variables:** Configurable via environment section (e.g., MCP_SERVER_PORT, LANG)
- **Health Checks:** Basic health checks ensure the service is running correctly
- **Restart Policy:** Configured for automatic restarts on failure

## 🤝 Contributing
Contributions are welcome! Please follow these guidelines:

- **Reporting:** Open an issue for bugs, feature requests, or suggestions
- **Branching:** Use feature branches (e.g., feature/new-analysis) for new development
- **Code Style:** Adhere to PEP 8
- **Testing:** Write unit and integration tests for new functionality
- **Pull Requests:** Submit pull requests to the main branch with clear descriptions

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.