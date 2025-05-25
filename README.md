# Enhanced Sequential Thinking Server 🧠

An advanced Model Context Protocol (MCP) server designed to facilitate and enhance the structured thinking processes of Large Language Models (LLMs). It provides a robust framework for reasoning chains, tree-like thought structures, metacognitive analysis, and adaptive planning.

## 👨‍💻 Author
[Vitaly Malakanov](https://github.com/VitalyMalakanov)

## 🚀 Project Status
![Stable](https://img.shields.io/badge/status-stable-green.svg)
![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

*   **Tree-structured Thoughts:** Support for branching and merging complex ideas.
*   **Metacognitive Analysis:** Deep insights into the quality and process of reasoning.
*   **Logical Consistency Checking:** Automatic identification of contradictions and coherence issues.
*   **Adaptive Planning:** Dynamic adjustment of thinking strategies based on context and effectiveness.
*   **Confidence & Quality Assessment:** Evaluation of thought clarity, evidence strength, and novelty.
*   **Cognitive Bias Detection:** Automated identification of common reasoning biases.
*   **Session Management:** Tools for exporting and analyzing entire thinking sessions.
*   **Multi-language Support:** Localized outputs and analysis markers via `localization.py` and `localization_markers.py`.

## 📦 Installation

### Prerequisites
Before you begin, ensure you have the following installed:
*   [Python 3.13+](https://www.python.org/downloads/)
*   [pip](https://pip.pypa.io/en/stable/installation/) (usually comes with Python)
*   [Docker](https://docs.docker.com/get-docker/) (for Docker installation)

### Local Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/VitalyMalakanov/nhanced_sequential_thinking_server.git
    cd nhanced_sequential_thinking_server
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ./venv/Scripts/activate # On Windows
    source venv/bin/activate # On macOS/Linux
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: `requirements.txt` should contain all listed dependencies including `mcp`, `colorama`, `numpy`, `scikit-learn`, `textstat`, `sentence-transformers`, `pytest`, `pytest-asyncio`, `pydantic` etc.*

### Docker Installation
1.  **Build and start the container:**
    ```bash
    docker-compose up --build
    ```
    Or run in detached mode (`-d`):
    ```bash
    docker-compose up -d --build
    ```
2.  **Stop the container:**
    ```bash
    docker-compose down
    ```

## 🚀 Usage

### Running the Server Locally
Once dependencies are installed:
```bash
python enhanced_sequential_thinking_server.py
```
The server will be available at http://localhost:8000/sse. Check the console output for the exact URL.

### Running the Server with Docker
If you started the server using docker-compose up, it will be available at: http://localhost:5000/sse
To change the default port (e.g., to 8080), modify the MCP_SERVER_PORT environment variable in docker-compose.yml or set it when running the command:
MCP_SERVER_PORT=8080 docker-compose up
Use code with caution.
Bash
Language Selection
By default, the server's console output and analysis messages are in English. To switch to Russian:
Local Run
You can modify the DEFAULT_LANG in localization.py or set it programmatically in enhanced_sequential_thinking_server.py's if __name__ == "__main__": block:
# In enhanced_sequential_thinking_server.py, near the end:
if __name__ == "__main__":
    import os
    server_lang = os.environ.get("LANG", "en").split('_').lower()
    if server_lang not in TRANSLATIONS:
        server_lang = "en" # Fallback to English
    server.set_language(server_lang)
    # ... rest of the main block ...
Use code with caution.
Python
Then run with LANG=ru environment variable:
LANG=ru python enhanced_sequential_thinking_server.py
Use code with caution.
Bash
Docker Run
Set the LANG environment variable in your docker-compose.yml file under the environment section for the mcp-server service:
# docker-compose.yml
services:
  mcp-server:
    # ...
    environment:
      - LANG=ru
    # ...
Use code with caution.
Yaml
Or set it directly when running docker-compose:
LANG=ru docker-compose up
Use code with caution.
Bash
Client Interaction Example
To interact with the running server, you can use a client like mcp.client.session.ClientSession. The provided tests (tests/test_client_interaction.py) serve as excellent examples of how to call the server's tools.
Here's a conceptual example using the mcp.client library (similar to what's in the test):
import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from enhanced_sequential_thinking_server import EnhancedThinkingInput, ThoughtType, ThinkingStrategy

async def main():
    server_url = "http://localhost:8000/sse" # Adjust port if different
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
            if result and result and result.text:
                print(json.dumps(json.loads(result.text), indent=2))
            else:
                print("No result or empty result.")

            # Call analyze_thinking_session
            print("\nCalling 'analyze_thinking_session'...")
            analysis_result = await session.call_tool("analyze_thinking_session")
            if analysis_result and analysis_result and analysis_result.text:
                print(json.dumps(json.loads(analysis_result.text), indent=2))

    except Exception as e:
        print(f"Error during client interaction: {e}")

if __name__ == "__main__":
    asyncio.run(main())
Use code with caution.
Python
🧪 Testing
The project includes client-side integration tests to ensure the server's tools function correctly.
Ensure the server is running (either locally or via Docker) on the configured port (e.g., http://localhost:8000).
Install test dependencies (if not already done via requirements.txt):
pip install pytest pytest-asyncio
Use code with caution.
Bash
Configure pytest-asyncio:
Create or edit pytest.ini in the project root (./pytest.ini):
[pytest]
asyncio_mode = strict
asyncio_default_fixture_loop_scope = module
Use code with caution.
Ini
Run tests:
Local Testing
pytest tests/test_client_interaction.py -v -s
Use code with caution.
Bash
(-v for verbose output, -s to show print statements from tests which include useful debug info from the client).
Docker Testing
(This requires the server to be running in one Docker Compose service, and the tests to be run from another service or within the same service, but accessing the server's port.)
Assuming your docker-compose.yml maps ports correctly and provides Python environment:
# If tests are in a separate service or need to run after server is up:
docker-compose run --rm mcp-server pytest tests/test_client_interaction.py -v -s
Use code with caution.
Bash
Note: Adjust mcp-server to your service name in docker-compose.yml if different.
�� Project Structure
- `enhanced_sequential_thinking_server.py`: The main server application and core thought analysis logic
- `localization.py`: Centralized translations and language support utilities
- `localization_markers.py`: Language-dependent markers and patterns for analysis
- `requirements.txt`: Python package dependencies
- `Dockerfile`: Docker image definition for the server
- `docker-compose.yml`: Docker Compose configuration for easy multi-service deployment
- `.dockerignore`: Specifies files and directories to exclude from the Docker build context
- `README.md`: This documentation file

🐳 Docker Configuration
The project includes Docker support for easy deployment and consistent environments. Key aspects:
Base Image: Uses a lightweight Python 3.13 slim image.
Port Mapping: Default internal server port 5000 is exposed (e.g., 5000:5000 in docker-compose.yml).
Volume Mounts: Allows for persistence of logs (e.g., /app/logs).
Environment Variables: Configurable via environment section (e.g., MCP_SERVER_PORT, LANG).
Health Checks: Basic health checks ensure the service is running correctly.
Restart Policy: Configured for automatic restarts on failure.
🤝 Contribution & Publishing
Contributions are welcome! Please follow these guidelines:
Reporting: Open an issue for bugs, feature requests, or suggestions.
Branching: Use feature branches (e.g., feature/new-analysis) for new development.
Code Style: Adhere to PEP 8.
Testing: Write unit and integration tests for new functionality, ensuring existing tests pass.
Pull Requests: Submit pull requests to the main branch, providing clear descriptions.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.