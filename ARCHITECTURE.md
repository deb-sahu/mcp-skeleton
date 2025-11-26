# MCP Skeleton - System Architecture

## 📐 Overview

This document provides technical architecture details for the MCP Skeleton template. For usage instructions, see [README.md](README.md).

**🎯 Key Principle**: This is a **SKELETON/TEMPLATE** - NOT a production application. The included tools (calculator, weather, HTTP, text) are **demonstration examples only**. You should replace them with your own domain-specific business logic while keeping the robust server infrastructure unchanged.

**Architecture Principle**: Complete separation between MCP server infrastructure (generic, reusable) and business logic (domain-specific, replaceable).

**Three-Layer Design**:
1. **Server Layer** (`mcp_server.py`) - Generic MCP protocol handling
2. **Business Logic** (`tools/`) - Your domain-specific implementations
3. **Utilities** (`utilities/`) - Shared configuration and helpers

**🔄 Use This Template For**:
- Database query interfaces
- ML/AI model inference endpoints
- Business rule engines
- API aggregation services
- Data processing pipelines
- Custom enterprise integrations
- Any domain-specific MCP server

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
├── pyproject.toml             # Poetry dependencies
├── poetry.lock                # Locked dependencies
├── Dockerfile                 # Production container image
├── entrypoint.sh              # Container entrypoint
├── .env.example               # Environment configuration template
├── ARCHITECTURE.md            # System architecture documentation
└── README.md                  # User guide and quick reference
```

## 🎯 Architecture Diagram

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         MCP Clients                              │
│  (Cursor, VS Code, Claude Desktop, Custom Clients)              │
└────────────────┬───────────────────────┬────────────────────────┘
                 │                       │
                 │ stdio                 │ HTTP/SSE
                 │                       │
┌────────────────▼───────────────────────▼────────────────────────┐
│                    MCP Skeleton Server                           │
│                     (mcp_server.py)                              │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              FastMCP Framework                           │   │
│  │  • Tool Registration                                     │   │
│  │  • Request Routing                                       │   │
│  │  • Transport Management (stdio/SSE)                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │       MCP Tool Registrations (@mcp.tool)                 │   │
│  │       Server layer routes to business logic              │   │
│  │  • tool_1() → calculator_tools.py                        │   │
│  │  • tool_2() → weather_tools.py                           │   │
│  │  • tool_3() → http_tools.py                              │   │
│  │  • tool_4() → text_tools.py                              │   │
│  └────────┬────────────┬──────────┬───────────┬─────────────┘   │
└───────────┼────────────┼──────────┼───────────┼─────────────────┘
            │            │          │           │
            ▼            ▼          ▼           ▼
┌───────────────────────────────────────────────────────────┐
│              Business Logic Layer (tools/)                 │
│     Isolated from server - plug in any custom logic        │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Tool 2     │  │  Tool 1      │  │  Tool 3      │     │
│  │  Weather    │  │  Calculator  │  │  HTTP        │     │
│  │  (Example)  │  │  (Example)   │  │  (Example)   │     │
│  │ • get_      │  │ • calculate_ │  │ • fetch_api_ │     │
│  │   weather_  │  │   operation  │  │   data       │     │
│  │   data()    │  │   ()         │  │   ()         │     │
│  └─────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
│  ┌─────────────┐  ┌──────────────────────────────────┐   │
│  │  Tool 4     │  │  Your Custom Tools               │   │
│  │  Text       │  │  (Tool 5, 6, 7...)               │   │
│  │  (Example)  │  │  Replace examples with:          │   │
│  │ • text_     │  │  • Database queries              │   │
│  │   analyzer  │  │  • ML inference                  │   │
│  │   ()        │  │  • Business rules                │   │
│  └─────────────┘  └──────────────────────────────────┘   │
└───────────────────────────────────────────────────────────┘
            │
            ▼
┌───────────────────────────────────────────────────────────┐
│                  Utilities Layer                           │
│                (utilities/ directory)                      │
│                                                             │
│  ┌──────────────────────┐  ┌────────────────────────┐    │
│  │  Configuration       │  │  Base Tools (legacy)   │    │
│  │  (config.py)         │  │  (base_tools.py)       │    │
│  │                      │  │                        │    │
│  │ • Settings           │  │ • BaseTools class      │    │
│  │ • Environment vars   │  │ • ToolResponse         │    │
│  │ • Pydantic models    │  │                        │    │
│  └──────────────────────┘  └────────────────────────┘    │
└───────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow

### Request Flow (stdio mode)

```
1. MCP Client (e.g., Cursor, VSCode Co-Pilot)
   ↓
2. Send tool request via stdio
   ↓
3. FastMCP Server receives request
   ↓
4. Route to appropriate @mcp.tool handler
   ↓
5. Handler calls tool implementation function
   ↓
6. Tool function executes logic
   ↓
7. Return result to handler
   ↓
8. Handler returns result to FastMCP
   ↓
9. FastMCP sends response via stdio
   ↓
10. Client receives result
```

### Request Flow (HTTP/SSE mode)

```
1. HTTP Client or MCP Client
   ↓
2. HTTP POST to /sse endpoint
   ↓
3. Uvicorn server receives request
   ↓
4. FastMCP routes via SSE transport
   ↓
5. Route to @mcp.tool handler
   ↓
6. Handler calls tool implementation
   ↓
7. Tool executes and returns result
   ↓
8. Response sent via SSE stream
   ↓
9. Client receives streaming response
```

## 🧩 Component Details

### 1. Server Layer (`mcp_server.py` at Root)

**Purpose**: MCP server initialization and tool registration

**Key File**:
- `mcp_server.py`: Main server entry point at project root

**Responsibilities**:
- Initialize FastMCP server with configuration
- Register all MCP tools using `@mcp.tool()` decorator
- Handle transport mode selection (stdio vs HTTP/SSE)
- Manage server lifecycle and logging
- **NO BUSINESS LOGIC** - only orchestration and registration

**Architecture Principle**:
The server layer is kept thin and generic. It does NOT contain business logic,
making this a reusable skeleton template for any MCP server implementation.

**Key Pattern**:
```python
# Tool registration wraps business logic from tools/ package
@mcp.tool()
async def calculator(operation: str, a: float, b: float) -> dict:
    """Mathematical operations tool."""
    # Server only orchestrates - business logic in tools/calculator_tools.py
    return await calculate_operation(operation, a, b)
```

### 2. Tools Layer (`tools/`)

**Purpose**: Contains ALL business logic, completely separated from server layer

**Architecture Principle**:
Business logic is segregated into modular, reusable tool implementations.
This makes the architecture GENERIC - not tied to weather, text, or any specific domain.
This is a SKELETON - replace example tools with your own domain-specific logic.

**📚 Example Tool Files** (⚠️ REPLACE THESE with your domain logic):
- `calculator_tools.py`: Tool 1 - Math operations example (DEMO ONLY)
- `weather_tools.py`: Tool 2 - API integration example (DEMO ONLY)
- `http_tools.py`: Tool 3 - HTTP client example (DEMO ONLY)
- `text_tools.py`: Tool 4 - Text processing example (DEMO ONLY)

**✨ Your Tool Files** (What you should create):
- `database_tools.py`: Database query operations
- `ml_inference_tools.py`: ML model prediction endpoints
- `business_logic_tools.py`: Domain-specific rules
- `api_integration_tools.py`: Third-party API connectors
- `data_processing_tools.py`: ETL and transformation logic
- ... any tool you need for your use case!

**Responsibilities**:
- Implement ALL core tool functionality
- Handle tool-specific error cases
- Return structured data
- Business logic lives here, NOT in server

**Design Pattern**: Simple async functions extracted from server
```python
# Tool implementation (business logic)
async def calculate_operation(operation: str, a: float, b: float) -> Dict[str, Any]:
    """Perform mathematical operation - ALL LOGIC HERE."""
    if operation == "add":
        result = a + b
    # ... more logic
    return {"operation": operation, "result": result}

# Server only calls this - no logic in mcp_server.py
```

**How Tools are Called**:
1. Tool implementation in `tools/your_tool.py` (business logic)
2. Export in `tools/__init__.py` 
3. Import in `mcp_server.py`
4. Wrap with `@mcp.tool()` decorator (registration only, no logic)
5. Server calls your function when MCP client requests it

### 3. Utilities Layer (`utilities/`)

**Purpose**: Shared configuration and utilities

**Key Files**:
- `config.py`: Settings management with Pydantic
- `base_tools.py`: Base classes (legacy, not used by current tools)

**Responsibilities**:
- Load and validate configuration from environment
- Provide shared utilities across tools
- Type-safe settings management

**Configuration Example**:
```python
class Settings(BaseSettings):
    server_name: str = "MCP Skeleton Server"
    mcp_server_host: str = "0.0.0.0"
    mcp_server_port: int = 8000
    log_level: str = "INFO"
```

## 🚀 Deployment Architecture

### Local Development

```
┌──────────────────┐
│  Developer       │
│  Machine         │
│                  │
│  ┌────────────┐ │
│  │ Python 3.10+│ │
│  │ Poetry      │ │
│  └────────────┘ │
│       │          │
│       ▼          │
│  ┌────────────┐ │
│  │ MCP Server │ │
│  │ (stdio)    │ │
│  └────────────┘ │
│       │          │
│       ▼          │
│  ┌────────────┐ │
│  │ MCP Client │ │
│  │ (Cursor/   │ │
│  │  VS Code)  │ │
│  └────────────┘ │
└──────────────────┘
```

### Container Deployment (AKS/Kubernetes)

```
┌─────────────────────────────────────────────────────────┐
│                    Kubernetes Cluster                    │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Ingress Controller                  │   │
│  │          (HTTPS/Load Balancer)                   │   │
│  └────────────────┬────────────────────────────────┘   │
│                   │                                      │
│                   ▼                                      │
│  ┌─────────────────────────────────────────────────┐   │
│  │               Service (ClusterIP)                │   │
│  │            Port: 8000 → 8000                     │   │
│  └────────────────┬────────────────────────────────┘   │
│                   │                                      │
│                   ▼                                      │
│  ┌─────────────────────────────────────────────────┐   │
│  │            Deployment (mcp-skeleton)             │   │
│  │                                                   │   │
│  │  ┌───────────────────────────────────────────┐ │   │
│  │  │         Pod 1                             │ │   │
│  │  │  ┌─────────────────────────────────────┐ │ │   │
│  │  │  │  Container: mcp-skeleton-server     │ │ │   │
│  │  │  │  Image: mcp-skeleton:latest         │ │ │   │
│  │  │  │  Port: 8000                         │ │ │   │
│  │  │  │  Protocol: HTTP/SSE                 │ │ │   │
│  │  │  │                                     │ │ │   │
│  │  │  │  Resources:                         │ │ │   │
│  │  │  │  • CPU: 100m-500m                   │ │ │   │
│  │  │  │  • Memory: 128Mi-512Mi              │ │ │   │
│  │  │  │                                     │ │ │   │
│  │  │  │  Health Checks:                     │ │ │   │
│  │  │  │  • Liveness: /sse                   │ │ │   │
│  │  │  │  • Readiness: /sse                  │ │ │   │
│  │  │  └─────────────────────────────────────┘ │ │   │
│  │  └───────────────────────────────────────────┘ │   │
│  │                                                   │   │
│  │  ┌───────────────────────────────────────────┐ │   │
│  │  │         Pod 2 (Replica)                   │ │   │
│  │  │  ... (same as Pod 1)                      │ │   │
│  │  └───────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────┘   │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │            ConfigMap / Secrets                   │   │
│  │  • SERVER_NAME                                   │   │
│  │  • LOG_LEVEL                                     │   │
│  │  • MCP_SERVER_HOST                               │   │
│  │  • MCP_SERVER_PORT                               │   │
│  │  • API Keys (if needed)                          │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## 🔒 Security Architecture

### Container Security

```
┌──────────────────────────────────────────────┐
│         Container Security Layers             │
│                                               │
│  1. Base Image                                │
│     └─ python:3.12-slim (minimal)            │
│                                               │
│  2. Non-root User                             │
│     └─ mcpuser (UID: 10001)                  │
│                                               │
│  3. File Permissions                          │
│     └─ All files owned by mcpuser            │
│                                               │
│  4. No Privileged Access                      │
│     └─ USER mcpuser in Dockerfile            │
│                                               │
│  5. Health Checks                             │
│     └─ Periodic endpoint monitoring          │
│                                               │
│  6. Read-only Filesystem (optional)           │
│     └─ Can be enforced in K8s                │
└──────────────────────────────────────────────┘
```

### Network Security

```
Internet
    │
    ▼
┌───────────────┐
│   Firewall    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Load Balancer │
│  (HTTPS/TLS)  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Ingress     │
│  (SSL Term)   │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Service     │
│  (ClusterIP)  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  MCP Server   │
│  (Port 8000)  │
└───────────────┘
```

## 📊 Tool Architecture

### Tool Implementation Pattern

Each tool follows a consistent pattern:

```
┌─────────────────────────────────────────────┐
│         Tool Implementation Pattern          │
│                                              │
│  1. Async Function                           │
│     async def tool_name(...) -> Dict         │
│                                              │
│  2. Type Hints                               │
│     All parameters and returns typed         │
│                                              │
│  3. Docstring                                │
│     Clear description and args               │
│                                              │
│  4. Error Handling                           │
│     Try/except with meaningful errors        │
│                                              │
│  5. Structured Response                      │
│     Dictionary with consistent keys          │
│                                              │
│  6. Logging (optional)                       │
│     Log important operations                 │
└─────────────────────────────────────────────┘
```

### Tool Response Format

```python
# Success Response
{
    "operation": "add",
    "operand_a": 5,
    "operand_b": 3,
    "result": 8
}

# Error Response (raised as exception)
raise ValueError("Division by zero is not allowed")
```

## 🔧 Configuration Architecture

### Environment Configuration Flow

```
.env file
    │
    ▼
┌─────────────────┐
│  Environment    │
│  Variables      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Pydantic       │
│  Settings       │
│  (config.py)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Validated      │
│  Configuration  │
│  Object         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Server &       │
│  Tools Usage    │
└─────────────────┘
```

### Configuration Layers

```
┌────────────────────────────────────────┐
│     Configuration Priority             │
│  (Highest to Lowest)                   │
│                                         │
│  1. Environment Variables               │
│     (Set in shell or K8s)              │
│         ↓                               │
│  2. .env File                           │
│     (Local development)                │
│         ↓                               │
│  3. Default Values                      │
│     (In config.py)                     │
└────────────────────────────────────────┘
```

## 🚦 Transport Modes

### stdio Transport

```
MCP Client (Cursor/VS Code)
    │
    │ stdin/stdout pipes
    │
    ▼
MCP Server Process
    │
    │ Direct function calls
    │
    ▼
Tool Implementations
```

**Use Cases**:
- Local development
- IDE integration (Cursor, VS Code)
- Direct client-server communication
- Desktop applications

**Activation**: `python mcp_server.py` (default)

### HTTP/SSE Transport

```
HTTP Client/MCP Client
    │
    │ HTTP POST
    │
    ▼
Uvicorn ASGI Server
    │
    │ Server-Sent Events
    │
    ▼
FastMCP SSE Handler
    │
    │ Event streaming
    │
    ▼
Tool Implementations
```

**Use Cases**:
- Container deployments
- Kubernetes/AKS
- Cloud environments
- Web-based clients
- Multiple concurrent clients

**Activation**: `python mcp_server.py --http`

## 📦 Dependency Management

### Poetry Dependency Graph

```
mcp-skeleton
├── fastmcp ^0.2.0
│   └── mcp (transitive)
├── pydantic ^2.11.7
├── pydantic-settings ^2.9.1
│   └── pydantic
├── httpx >=0.27
├── python-dotenv ^1.0.0
└── uvicorn >=0.31.1

Dev Dependencies:
├── pytest ^7.0.0
├── pytest-asyncio ^0.21.0
├── black ^24.0.0
├── ruff ^0.1.0
└── mypy ^1.0.0
```

## 🔄 Extension Points

### Adding Your Business Logic (New Tools)

**The 3-Layer Separation**:

```
1. Business Logic Layer (tools/)
   Create: tools/tool_5.py (or tools/my_business_logic.py)
   
   async def my_business_function(input_data) -> Dict:
       """Your business logic here - DB, ML, APIs, etc."""
       # This is where YOUR code goes
       result = process_your_data(input_data)
       return {"result": result}

2. Export Layer (tools/__init__.py)
   Add to __all__:
   
   __all__ = [
       'calculate_operation',    # Tool 1 (example)
       'get_weather_data',       # Tool 2 (example)
       'my_business_function',   # Tool 5 (yours)
   ]

3. Server Layer (mcp_server.py) - Generic routing only
   Register tool (server just delegates):
   
   @mcp.tool()
   async def tool_5(input_data: str) -> dict:
       """Tool 5: Your custom logic."""
       # Server layer just routes - no business logic here
       return await my_business_function(input_data)

4. Test and deploy
   Your business logic is now accessible via MCP protocol!
```

**Key Point**: The server layer (`mcp_server.py`) remains generic. All your custom code goes in `tools/`.

### Adding New Configuration

```
1. Update utilities/config.py
   class Settings(BaseSettings):
       my_new_setting: str = "default"

2. Add to .env.example
   MY_NEW_SETTING=value

3. Use in code
   from utilities.config import settings
   value = settings.my_new_setting
```

## 🎭 Scalability Considerations

### Horizontal Scaling

```
┌─────────────────────────────────────────┐
│         Load Balancer                    │
└────┬──────────┬──────────┬──────────────┘
     │          │          │
     ▼          ▼          ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│ Pod 1   │ │ Pod 2   │ │ Pod 3   │
│ MCP     │ │ MCP     │ │ MCP     │
│ Server  │ │ Server  │ │ Server  │
└─────────┘ └─────────┘ └─────────┘
```

**Considerations**:
- Stateless design (no session storage)
- Each pod is independent
- Can scale from 1 to N replicas
- Health checks for auto-healing

### Resource Optimization

```
Resource Profiles:

Small (Development):
  CPU: 100m-250m
  Memory: 128Mi-256Mi
  Replicas: 1

Medium (Staging):
  CPU: 250m-500m
  Memory: 256Mi-512Mi
  Replicas: 2

Large (Production):
  CPU: 500m-1000m
  Memory: 512Mi-1Gi
  Replicas: 3+
```

## 📈 Monitoring Architecture

### Observability Stack

```
┌─────────────────────────────────────────┐
│           Application Logs               │
│     (stdout/stderr via logging)         │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│        Container Runtime Logs            │
│          (Docker/containerd)            │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│       Kubernetes Logging Stack           │
│    (Fluentd/Fluent Bit → Storage)       │
└─────────────────────────────────────────┘
```

### Health Check Flow

```
K8s Liveness Probe
    │
    │ Every 30s
    │
    ▼
curl http://localhost:8000/sse
    │
    ├─ Success (200) → Healthy
    │
    └─ Failure/Timeout → Restart Pod
```

## 🔬 Testing Strategy

### Test Pyramid

```
┌─────────────────────────────────┐
│      End-to-End Tests           │
│   (Full MCP client flows)       │
└─────────────┬───────────────────┘
              │
┌─────────────▼───────────────────┐
│       Integration Tests         │
│  (Server + Tools together)      │
└─────────────┬───────────────────┘
              │
┌─────────────▼───────────────────┐
│         Unit Tests              │
│   (Individual tool functions)   │
└─────────────────────────────────┘
```

## 🚀 CI/CD Pipeline

```
1. Code Commit (Git)
   ↓
2. Run Tests (pytest)
   ↓
3. Lint & Format (black, ruff, mypy)
   ↓
4. Build Docker Image
   ↓
5. Push to Registry
   ↓
6. Deploy to K8s (kubectl apply)
   ↓
7. Health Check
   ↓
8. Monitor
```

## 📝 Summary

The MCP Skeleton architecture provides:

✅ **Modular Design**: Clear separation between servers, tools, and utilities
✅ **Flexible Transport**: Support for both stdio and HTTP/SSE
✅ **Production Ready**: Docker, Kubernetes, security best practices
✅ **Type Safe**: Pydantic models for configuration and validation
✅ **Extensible**: Easy to add new tools and features
✅ **Observable**: Logging, health checks, and monitoring hooks
✅ **Scalable**: Stateless design for horizontal scaling

This architecture supports development from local prototyping through to enterprise production deployments on Kubernetes/AKS.
