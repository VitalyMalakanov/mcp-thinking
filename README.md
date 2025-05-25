# Enhanced Sequential Thinking Server

**Enhanced MCP Server** — advanced tool for structured LLM thinking with quality analysis, cognitive bias detection, and multiple thinking strategies.

## Features
- Tree-structured thoughts with branching and merging
- Metacognitive analysis
- Logical consistency checking
- Adaptive planning
- Confidence and quality assessment
- Cognitive bias detection
- Session export and analysis

## Installation

### Local Installation
```bash
pip install -r requirements.txt
```

### Docker Installation
```bash
# Build and start the container
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build

# Stop the container
docker-compose down
```

## Running the Server

### Local Run
```bash
python enhanced_sequential_thinking_server.py
```

### Docker Run
The server will be available at: http://localhost:5000/sse

To change the port, modify the `MCP_SERVER_PORT` environment variable in `docker-compose.yml` or set it when running:
```bash
MCP_SERVER_PORT=8080 docker-compose up
```

### Language selection
By default, the interface and output are in English. To use Russian:

#### Local Run
```python
from enhanced_sequential_thinking_server import EnhancedThinkingServer
server = EnhancedThinkingServer(language="ru")
```

#### Docker Run
Set the `LANG` environment variable in `docker-compose.yml` or when running:
```bash
LANG=ru docker-compose up
```

## Testing
```bash
# Local testing
pytest tests/

# Docker testing
docker-compose run --rm mcp-server pytest tests/
```

## Project Structure
- `enhanced_sequential_thinking_server.py` — main server and thought analysis logic
- `tests/` — smoke and regression tests
- `requirements.txt` — project dependencies
- `README.md` — documentation and instructions
- `localization.py` — translations and language support
- `Dockerfile` — Docker image configuration
- `docker-compose.yml` — Docker Compose configuration
- `.dockerignore` — files to exclude from Docker build

## Docker Configuration
The project includes Docker support for easy deployment and consistent environments:

- `Dockerfile` uses Python 3.13 slim image
- `docker-compose.yml` configures the service with:
  - Port mapping (default: 5000)
  - Volume mounts for logs
  - Environment variables for language and port
  - Health checks
  - Automatic restart policy

## Contribution & Publishing
- Use `.gitignore` to exclude temp files, logs, and virtual environments
- Use branches for new features
- Write tests for new functionality
- MIT License

---

## Author
**Author:** [Your Name] 