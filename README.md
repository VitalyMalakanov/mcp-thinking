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

### Client Interaction Example
```python
import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from enhanced_sequential_thinking_server import (
    EnhancedThinkingInput,
    ThoughtType,
    ThinkingStrategy
)

async def main():
    server_url = "http://localhost:8000/sse"  # Adjust port if different
    print(f"Connecting to MCP server at {server_url}")

    try:
        async with sse_client(url=server_url, timeout=10) as (read_stream, write_stream):
            session = ClientSession(read_stream, write_stream)
            await session.initialize()
            print("MCP session initialized. Calling tool...")

            # Call enhanced_thinking tool
            input_data = EnhancedThinkingInput(
                thought="Consider the impact of decentralized autonomous organizations (DAOs) on traditional corporate governance models.",
                thought_type=ThoughtType.ANALYSIS,
                strategy=ThinkingStrategy.SYSTEMIC,
                tags=["DAO", "governance", "blockchain"]
            )
            result = await session.call_tool("enhanced_thinking", input_data)
            
            print("\nTool 'enhanced_thinking' result:")
            if result and result[0].text:
                print(json.dumps(json.loads(result[0].text), indent=2))
            else:
                print("No result or empty result.")

    except Exception as e:
        print(f"Error during client interaction: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

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