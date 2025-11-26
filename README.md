# MCP Skeleton - MCP Server Template (Python)

> **🎯 This is a SKELETON/TEMPLATE for building MCP servers - NOT a production application!**  

MCP Skeleton is a **generic template** for building Model Context Protocol (MCP) servers with FastMCP. The architecture provides complete separation between the MCP server layer and your business logic, making it a true "plug-and-play" skeleton for any domain.

Provides a modular architecture for building production-ready MCP servers with dual transport modes (stdio + HTTP/SSE) and full Kubernetes/AKS deployment support.

## ✨ Key Features

- **Clean Structure** – Flat file organization with clear separation of concerns
- **Dual Transport** – Supports both stdio (IDE integration) and HTTP/SSE (deployment)
- **Structured Responses** – Consistent JSON responses across all tools
- **Type Safe** – Pydantic models for request/response validation
- **Example Tools** – Calculator and weather services as reference implementations
- **Production Ready** – Includes Docker setup and configuration management

---

## 🏗️ Project Structure

```
mcp-skeleton/
├── mcp_server.py              # Main MCP server with tool registrations
│
├── tools/                      # Business Logic Layer ⚠️ REPLACE WITH YOUR OWN
│   ├── __init__.py            # Package exports (required)
│   ├── calculator_tools.py    # 📚 EXAMPLE Tool 1: Math operations (replace)
│   ├── weather_tools.py       # 📚 EXAMPLE Tool 2: Weather data (replace)
│   ├── http_tools.py          # 📚 EXAMPLE Tool 3: API integration (replace)
│   ├── text_tools.py          # 📚 EXAMPLE Tool 4: Text processing (replace)
│   └── your_tool.py           # ✨ YOUR Tool 5+: Custom business logic
│
├── utilities/                  # Shared Utilities (Keep as-is or extend)
│   ├── __init__.py            # Package exports (required)
│   ├── config.py              # Configuration management
│   └── base_tools.py          # Base classes for consistent responses
│
├── tests/                      # Test Cases ⚠️ REPLACE WITH YOUR OWN
│   ├── __init__.py            # Test package initialization
│   ├── conftest.py            # Pytest fixtures and configuration
│   ├── test_calculator_tools.py  # 📚 EXAMPLE: Calculator tests (replace)
│   ├── test_weather_tools.py     # 📚 EXAMPLE: Weather tests (replace)
│   ├── test_text_tools.py        # 📚 EXAMPLE: Text analysis tests (replace)
│   └── test_your_tools.py        # ✨ YOUR tests for your tools
│
├── pyproject.toml             # Poetry dependencies
├── poetry.lock                # Locked dependencies (commit this!)
├── Dockerfile                 # Production container image
├── entrypoint.sh              # Container entrypoint
├── .env.example               # Environment configuration template
├── ARCHITECTURE.md            # System architecture documentation
└── README.md                  # User guide and quick reference
```

> **Note**: 
> - `__init__.py` files are required for Python to recognize directories as packages
> - 📚 EXAMPLE files are demonstrations - replace with your own implementations
> - ✨ YOUR files represent what you should create for your domain
> - Run tests with `poetry run pytest`

## 🚀 What This Template Provides

✅ **Production-Ready Infrastructure** (Keep as-is)
- MCP server with FastMCP framework
- Dual transport: stdio (local) + HTTP/SSE (containers)
- Docker containerization with security best practices
- Kubernetes/AKS deployment configurations
- Type-safe configuration with Pydantic
- Comprehensive logging and health checks

📚 **Example Tools** (Replace with your business logic)
- Calculator, Weather, HTTP, Text tools are **DEMOS ONLY**
- Shows the pattern for implementing your own tools
- Clear separation between server and business logic

## ⚠️ Before You Start

**This template includes 4 example tools that you should REPLACE:**

| Example Tool | Purpose | Replace With |
|--------------|---------|--------------|
| 🧮 Calculator | Math operations demo | Your domain logic |
| 🌤️ Weather | API integration pattern | Your API calls |
| 🌐 HTTP | HTTP client example | Your integrations |
| 📝 Text | Text processing demo | Your data processing |

**Keep:** Server infrastructure, Docker, Kubernetes configs, utilities  
**Replace:** Everything in `tools/` directory with your business logic

## 📋 Template Features

### 🏗️ Production Infrastructure (Keep These)
- **Modular Architecture**: Clean 3-layer separation (Server → Tools → Utilities)
- **Dual Transport Modes**: 
  - **stdio**: For local development with MCP clients (Cursor, VS Code, Claude Desktop)
  - **HTTP/SSE**: For production deployments (Docker, Kubernetes, AKS, cloud)
- **Enterprise-Grade Docker**: Multi-stage build, non-root user, health checks, security best practices
- **Kubernetes/AKS Ready**: Deployment manifests, horizontal scaling, observability, production patterns
- **Type Safety**: Pydantic models for configuration validation
- **Poetry Dependency Management**: Modern Python packaging with lockfile
- **Comprehensive Logging**: Structured logging with configurable levels

### 📚 Example Implementations (Replace These)
- **4 Demo Tools**: Calculator, Weather (mock), HTTP client, Text analysis
- **Clear Patterns**: Shows how to structure async functions, error handling, responses
- **Documentation**: Extensive comments explaining the architecture
- **Easy to Remove**: Simply delete example tools and add your own

## 🚀 Quick Start

### Local Development with Poetry

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Run the server:**
   
   **stdio mode** (for Cursor, VS Code):
   ```bash
   poetry run python mcp_server.py
   # or use the entry point
   poetry run mcp-skeleton
   ```

   **HTTP/SSE mode** (for containers/web):
   ```bash
   poetry run python mcp_server.py --http
   ```
   
   Server available at `http://localhost:8000/sse`

### Docker Deployment

1. **Build the image:**
   ```bash
   docker build -t mcp-skeleton:latest .
   ```

2. **Run the container:**
   ```bash
   docker run -d \
     -p 8000:8000 \
     -e LOG_LEVEL=INFO \
     --name mcp-skeleton \
     mcp-skeleton:latest
   ```

3. **Test the endpoint:**
   ```bash
   curl http://localhost:8000/sse
   ```

### Kubernetes/AKS Deployment

See [ARCHITECTURE.md](ARCHITECTURE.md) for complete Kubernetes deployment examples including:
- Deployment manifests
- Service configuration
- Ingress setup
- ConfigMaps and Secrets
- Resource limits and scaling

## 🛠️ Example Tools (⚠️ REPLACE with Your Business Logic)

> **🎯 These are DEMONSTRATION TOOLS ONLY** - They show you the pattern, but are not meant for production use.  
> Delete or replace them with your domain-specific business logic.

| Demo Tool | What It Shows | Replace With Your... |
|-----------|---------------|---------------------|
| 🧮 **Calculator** | Basic async function with validation | Database queries, computations, business rules |
| 🌤️ **Weather** (mock) | External API pattern (mock implementation) | Real API integrations, third-party services |
| 🌐 **HTTP** | HTTP client usage with httpx | API aggregation, webhook handlers, integrations |
| 📝 **Text** | String processing and analysis | NLP, data transformation, ETL logic |

### What You Should Build Instead

Replace the example tools with **your actual use case**:

| Use Case | Your Tools | Example |
|----------|-----------|---------|
| **Database Interface** | `query_tools.py`, `analytics_tools.py` | PostgreSQL queries, aggregations |
| **ML/AI Platform** | `inference_tools.py`, `training_tools.py` | Model predictions, embeddings |
| **Business Logic** | `validation_tools.py`, `rules_tools.py` | Pricing engines, approval workflows |
| **Data Processing** | `etl_tools.py`, `transform_tools.py` | Data pipelines, format converters |
| **API Gateway** | `integration_tools.py`, `orchestration_tools.py` | Service mesh, API composition |

### Tool Response Format

All tools return structured dictionaries. Design your responses based on your use case:

```python
# ❌ Example Tool Response (Calculator - Demo, replace this)
{
    "operation": "add",
    "operand_a": 5,
    "operand_b": 3,
    "result": 8
}

# ✅ Your Custom Tool Response (Database Query)
{
    "query": "SELECT * FROM users WHERE active = true",
    "results": [...],
    "count": 42,
    "execution_time_ms": 23
}

# ✅ Your Custom Tool Response (ML Inference)
{
    "model": "sentiment-analyzer-v2",
    "input_text": "This product is amazing!",
    "prediction": "positive",
    "confidence": 0.94,
    "inference_time_ms": 156
}

# ✅ Your Custom Tool Response (Business Logic)
{
    "rule": "pricing_engine",
    "base_price": 100.0,
    "discount_applied": 15.0,
    "final_price": 85.0,
    "currency": "USD"
}
```

## ➕ How to Use This Template

### Quick Start: Replace Example Tools with Your Logic

**Architecture Principle**: Business logic lives in `tools/`, server infrastructure stays in `mcp_server.py`.  
This separation keeps the template generic and your code modular.

### Option 1: Clean Slate (Recommended for New Projects)

1. **Delete all example tools:**
   ```bash
   rm tools/calculator_tools.py tools/weather_tools.py tools/http_tools.py tools/text_tools.py
   ```

2. **Create your first tool:**
   ```bash
   touch tools/your_domain_tools.py
   ```

3. **Implement your business logic** (see Step 1 below)

### Option 2: Incremental Replacement (Keep Examples as Reference)

Keep example tools while building your own, then remove them later.

---

### Step 1: Create Tool Implementation (Your Business Logic)

```python
# tools/your_domain_tools.py (e.g., database_tools.py, ml_tools.py, etc.)
from typing import Dict, Any

async def your_business_function(input_param: str) -> Dict[str, Any]:
    """
    Your actual business logic implementation.
    
    Real-world examples:
    - Database query: await db.execute(query)
    - ML inference: model.predict(input_param)
    - API call: await httpx.get(external_api)
    - Business rule: calculate_pricing(input_param)
    - Data processing: transform_data(input_param)
    """
    # ✅ Replace this with YOUR ACTUAL implementation
    # Example: Database query
    # results = await db.query("SELECT * FROM table WHERE id = ?", input_param)
    
    # Example: ML inference
    # prediction = await ml_model.predict(input_param)
    
    # Example placeholder (replace this):
    processed_result = f"Processed: {input_param}"
    
    return {
        "input": input_param,
        "result": processed_result,
        "status": "success",
        "metadata": {
            "processed_at": "2024-01-01T00:00:00Z",
            "version": "1.0"
        }
    }
```

### Step 2: Export in `tools/__init__.py`

```python
# tools/__init__.py

# ❌ Remove or comment out example tools:
# from .calculator_tools import calculate_operation
# from .weather_tools import get_weather_data
# from .http_tools import fetch_api_data
# from .text_tools import text_analyzer

# ✅ Import YOUR tools:
from .your_domain_tools import your_business_function
# from .database_tools import query_database, insert_record
# from .ml_tools import run_inference, get_embeddings
# from .api_tools import fetch_external_data

__all__ = [
    # Your tool functions
    'your_business_function',
    # 'query_database',
    # 'insert_record',
    # 'run_inference',
    # 'get_embeddings',
    # 'fetch_external_data',
]
```

### Step 3: Register in `mcp_server.py` (Server Layer - Thin Wrapper Only!)

```python
# mcp_server.py

# ❌ Remove example tool imports:
# from tools.weather_tools import get_weather_data
# from tools.calculator_tools import calculate_operation

# ✅ Import YOUR tools:
from tools.your_domain_tools import your_business_function

# ❌ Delete or comment out example tool registrations:
# @mcp.tool()
# async def get_weather(city: str) -> dict: ...

# ✅ Register YOUR tool (server just routes, no business logic here!):
@mcp.tool()
async def your_tool_name(input_param: str) -> dict:
    """
    Your tool description that MCP clients will see.
    
    ⚠️ IMPORTANT: This function should ONLY delegate to your business logic.
    Do NOT put business logic here - keep it in tools/your_domain_tools.py
    
    Args:
        input_param: Description of your parameter
        
    Returns:
        Result from your business logic function
    """
    # Server layer just delegates - all logic in tools/ directory
    return await your_business_function(input_param)
```

**✅ That's it!** Your business logic is now accessible via MCP protocol.

**Key Architecture Points:**
- ✅ Server layer (`mcp_server.py`): Generic, reusable, thin routing only
- ✅ Business logic (`tools/`): Your domain-specific code, modular and testable
- ✅ Complete separation: Easy to maintain, extend, and test independently

## 🔧 Configuration

Configuration is managed via environment variables and `utilities/config.py`:

```python
# .env file (copy from .env.example)
SERVER_NAME=MCP Skeleton Server
SERVER_VERSION=0.1.0
LOG_LEVEL=INFO
MCP_SERVER_HOST=0.0.0.0
MCP_SERVER_PORT=8000
```

To add custom configuration:

1. **Update `utilities/config.py`:**
   ```python
   class Settings(BaseSettings):
       # Existing settings
       server_name: str = "MCP Skeleton Server"
       
       # Your new settings
       my_api_key: Optional[str] = None
       my_custom_setting: str = "default_value"
   ```

2. **Add to `.env.example`:**
   ```bash
   MY_API_KEY=your_api_key_here
   MY_CUSTOM_SETTING=some_value
   ```

3. **Use in your code:**
   ```python
   from utilities.config import settings
   
   api_key = settings.my_api_key
   ```

## 📦 Dependencies

Managed via Poetry in `pyproject.toml`:

**Core Dependencies:**
- `fastmcp ^0.2.0` - FastMCP framework
- `pydantic ^2.11.7` - Data validation
- `pydantic-settings ^2.9.1` - Settings management
- `httpx >=0.27` - HTTP client
- `python-dotenv ^1.0.0` - Environment variables
- `uvicorn >=0.31.1` - ASGI server

**Dev Dependencies:**
- `pytest ^7.0.0` - Testing framework
- `pytest-asyncio ^0.21.0` - Async testing
- `black ^24.0.0` - Code formatting
- `ruff ^0.1.0` - Linting
- `mypy ^1.0.0` - Type checking

To update dependencies:
```bash
poetry update
poetry lock
```

## 🧪 Development

### Code Quality

```bash
# Format code
poetry run black .

# Lint code
poetry run ruff check .

# Type checking
poetry run mypy mcp_server.py tools utilities

# Run all checks
poetry run black . && poetry run ruff check . && poetry run mypy mcp_server.py tools utilities
```

### Testing

Example tests are provided in the `tests/` directory showing patterns for testing async functions.

```bash
# Run all tests
poetry run pytest

# Run with verbose output
poetry run pytest -v

# Run with coverage
poetry run pytest --cov=tools --cov=utilities

# Run specific test file
poetry run pytest tests/test_calculator_tools.py

# Run tests matching a pattern
poetry run pytest -k "calculator"
```

**Replace example tests with your own:**
- `test_calculator_tools.py` → tests for your business logic
- `test_weather_tools.py` → tests for your API integrations
- `test_text_tools.py` → tests for your data processing
- Add `conftest.py` fixtures for your specific needs

## 🐳 Docker Production

### Build Arguments

```bash
# Custom Poetry version
docker build --build-arg POETRY_VERSION=1.8.0 -t mcp-skeleton:latest .
```

### Environment Variables

```bash
docker run -d \
  -p 8000:8000 \
  -e SERVER_NAME="My MCP Server" \
  -e LOG_LEVEL=DEBUG \
  -e MCP_SERVER_PORT=8000 \
  --name mcp-skeleton \
  mcp-skeleton:latest
```

### Security Features

- ✅ Non-root user (`mcpuser`, UID 10001)
- ✅ Minimal base image (`python:3.12-slim`)
- ✅ Multi-stage build with Poetry
- ✅ Health check endpoint
- ✅ Proper file permissions
- ✅ No hardcoded secrets

## ☸️ Kubernetes/AKS

### Quick Deploy

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-skeleton
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mcp-skeleton
  template:
    metadata:
      labels:
        app: mcp-skeleton
    spec:
      containers:
      - name: mcp-skeleton
        image: your-registry/mcp-skeleton:latest
        ports:
        - containerPort: 8000
        env:
        - name: LOG_LEVEL
          value: "INFO"
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /sse
            port: 8000
          initialDelaySeconds: 10
        readinessProbe:
          httpGet:
            path: /sse
            port: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: mcp-skeleton
spec:
  selector:
    app: mcp-skeleton
  ports:
  - port: 80
    targetPort: 8000
```

Deploy:
```bash
kubectl apply -f deployment.yaml
kubectl get pods -l app=mcp-skeleton
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for complete Kubernetes configuration including Ingress, ConfigMaps, Secrets, and scaling strategies.

## 📊 Monitoring & Observability

### Logs

```bash
# Docker logs
docker logs -f mcp-skeleton

# Kubernetes logs
kubectl logs -f deployment/mcp-skeleton
kubectl logs -f pod/mcp-skeleton-xxx

# Stream logs from all replicas
kubectl logs -f -l app=mcp-skeleton
```

### Health Checks

```bash
# Direct health check
curl http://localhost:8000/sse

# Check container health
docker inspect --format='{{.State.Health.Status}}' mcp-skeleton

# Kubernetes health
kubectl describe pod mcp-skeleton-xxx
```

### Metrics

Set `LOG_LEVEL=DEBUG` for detailed logging:
```bash
export LOG_LEVEL=DEBUG
poetry run python mcp_server.py --http
```

## 🚀 Production Checklist

Before deploying to production:

- [ ] Generate `poetry.lock`: `poetry lock`
- [ ] Update version in `pyproject.toml`
- [ ] Set appropriate `LOG_LEVEL` (INFO or WARNING)
- [ ] Configure resource limits in K8s
- [ ] Set up monitoring and alerting
- [ ] Configure log aggregation
- [ ] Add custom API keys to secrets
- [ ] Test health check endpoints
- [ ] Configure horizontal pod autoscaling
- [ ] Set up ingress with TLS
- [ ] Run security scan: `docker scan mcp-skeleton:latest`
- [ ] Load testing for expected traffic
- [ ] Document custom configurations

## 📚 Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Complete system architecture, diagrams, deployment strategies, security, and scalability
- **[.env.example](.env.example)** - Configuration template with all available options
- **[pyproject.toml](pyproject.toml)** - Project metadata and dependencies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run quality checks: `poetry run black . && poetry run ruff check .`
5. Commit: `git commit -m 'Add my feature'`
6. Push: `git push origin feature/my-feature`
7. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

## 💡 Quick Commands

```bash
# Development
poetry install                          # Install dependencies
poetry run python mcp_server.py        # Run stdio mode
poetry run python mcp_server.py --http # Run HTTP mode
poetry run mcp-skeleton                 # Run via entry point

# Docker
docker build -t mcp-skeleton .          # Build image
docker run -p 8000:8000 mcp-skeleton   # Run container
docker logs -f mcp-skeleton            # View logs

# Kubernetes
kubectl apply -f deployment.yaml        # Deploy
kubectl get pods                        # Check status
kubectl logs -f deployment/mcp-skeleton # Stream logs
kubectl scale deployment mcp-skeleton --replicas=3  # Scale

# Quality
poetry run black .                      # Format
poetry run ruff check .                 # Lint
poetry run mypy mcp_server.py          # Type check
```

---

## 🎯 Getting Started Checklist

Before using this template for your project:

- [ ] Update `pyproject.toml` with your name and email
- [ ] Update `SERVER_NAME` in `.env` or `utilities/config.py`
- [ ] Delete or replace example tools in `tools/`
- [ ] Update tool imports in `tools/__init__.py`
- [ ] Update tool registrations in `mcp_server.py`
- [ ] Update MCP server instructions in `mcp_server.py`
- [ ] Add your custom configuration to `utilities/config.py`
- [ ] Write tests for your tools in `tests/`
- [ ] Run tests to verify: `poetry run pytest`
- [ ] Update this README.md with your project details
- [ ] Test locally with `poetry run python mcp_server.py`
- [ ] Build and test Docker image
- [ ] Deploy to your target environment

---

**Template Version**: 0.1.0  
**Status**: Production Ready Template  
**Deployment**: Local, Docker, Kubernetes, AKS Compatible  
**License**: MIT (or your license)  

**⚠️ Remember**: This is a TEMPLATE. Update project metadata in `pyproject.toml` with your information!
