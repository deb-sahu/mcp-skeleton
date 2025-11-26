# MCP Skeleton Template - Usage Guide

> **Created**: This guide helps you use the MCP Skeleton template to build your own MCP server.

## 🎯 What Is This?

This is a **SKELETON/TEMPLATE** for building Model Context Protocol (MCP) servers - NOT a production application. The included tools (calculator, weather, HTTP, text) are **demonstration examples** showing patterns you should follow.

## ✅ Structure Review - Everything Looks Great!

Your MCP skeleton has been reviewed and all components are well-structured:

### Production-Ready Infrastructure (✅ Keep As-Is)
- ✅ Clean 3-layer architecture (Server → Tools → Utilities)
- ✅ Dual transport support (stdio + HTTP/SSE)
- ✅ Docker with security best practices (non-root user)
- ✅ Kubernetes/AKS deployment ready
- ✅ Type-safe configuration with Pydantic
- ✅ Comprehensive documentation
- ✅ Poetry dependency management

### Example Code (⚠️ Replace These)
- ⚠️ `tools/calculator_tools.py` - Math operations demo
- ⚠️ `tools/weather_tools.py` - API integration demo (mock)
- ⚠️ `tools/http_tools.py` - HTTP client demo
- ⚠️ `tools/text_tools.py` - Text processing demo

## 📝 Changes Made

### 1. Documentation Made Generic

**ARCHITECTURE.md**:
- ✅ Emphasized skeleton/template nature throughout
- ✅ Added clear labels for example vs. your tools
- ✅ Expanded use case examples (DB, ML, business logic, etc.)
- ✅ Clarified what to keep vs. what to replace

**README.md**:
- ✅ Prominent warnings that examples should be replaced
- ✅ Added comparison table: "Example Tools" vs. "What to Build"
- ✅ Step-by-step guide for replacing examples
- ✅ Real-world use case examples (DB queries, ML inference, etc.)
- ✅ Added "Getting Started Checklist"
- ✅ Removed domain-specific branding

### 2. Code Made Generic

**mcp_server.py**:
- ✅ Updated docstring to emphasize template nature
- ✅ Added comments marking example tool imports
- ✅ Updated MCP instructions with replacement reminder
- ✅ Added comprehensive comments in tool registration section
- ✅ Labeled each example tool with "[EXAMPLE TOOL]"
- ✅ Added template section for adding your own tools

**pyproject.toml**:
- ✅ Updated keywords (removed "weather", "calculator")
- ✅ Added generic keywords ("template", "skeleton", "enterprise")
- ✅ Changed author to placeholder
- ✅ Updated classifiers to include "Code Generators"

### 3. Configuration Files

**✅ Created `.env.example`**:
- Environment variable template
- Examples for common configurations (DB, API keys, etc.)
- Clear documentation and usage notes

## 🚀 How to Use This Template

### Step 1: Clone or Fork
```bash
git clone <your-repo>
cd mcp-skeleton
```

### Step 2: Customize Project Metadata
```bash
# Edit pyproject.toml
- Update: name, description, authors
- Update: keywords to match your domain
- Update: version for your project
```

### Step 3: Configure Environment
```bash
# Copy and customize environment
cp .env.example .env

# Edit .env with your settings
SERVER_NAME="Your MCP Server Name"
# Add your API keys, DB URLs, etc.
```

### Step 4: Replace Example Tools

**Option A: Clean Slate (Recommended)**
```bash
# Remove all example tools
rm tools/calculator_tools.py
rm tools/weather_tools.py
rm tools/http_tools.py
rm tools/text_tools.py

# Create your tools
touch tools/your_domain_tools.py
```

**Option B: Keep Examples as Reference**
```bash
# Rename examples to keep as reference
mkdir tools/examples
mv tools/*_tools.py tools/examples/

# Create your tools
touch tools/your_domain_tools.py
```

### Step 5: Implement Your Tools

Edit `tools/your_domain_tools.py`:
```python
from typing import Dict, Any

async def your_business_function(param: str) -> Dict[str, Any]:
    """
    Your actual business logic.
    Examples:
    - Database queries
    - ML model inference
    - API integrations
    - Business rules
    - Data processing
    """
    # YOUR CODE HERE
    result = await your_actual_logic(param)
    
    return {
        "status": "success",
        "result": result,
        "metadata": {...}
    }
```

### Step 6: Update Exports

Edit `tools/__init__.py`:
```python
# Remove example imports
# from .calculator_tools import calculate_operation
# from .weather_tools import get_weather_data

# Add your imports
from .your_domain_tools import your_business_function

__all__ = [
    'your_business_function',
    # Add more...
]
```

### Step 7: Register Your Tools

Edit `mcp_server.py`:
```python
# Remove example imports (around line 17-20)
# from tools.weather_tools import get_weather_data
# from tools.calculator_tools import calculate_operation

# Import your tools
from tools.your_domain_tools import your_business_function

# Remove example tool registrations (@mcp.tool() functions)
# Keep only the FastMCP setup and main() function

# Add your tool registrations
@mcp.tool()
async def your_tool_name(param: str) -> dict:
    """Your tool description for MCP clients."""
    return await your_business_function(param)
```

### Step 8: Update Server Instructions

Edit `mcp_server.py` around line 39:
```python
mcp = FastMCP(
    name=settings.server_name,
    instructions=(
        "Your server description. Explain what tools you provide "
        "and what capabilities your MCP server offers."
    )
)
```

### Step 9: Test Locally

**stdio mode (for Cursor/VS Code):**
```bash
poetry install
poetry run python mcp_server.py
```

**HTTP/SSE mode (for containers):**
```bash
poetry run python mcp_server.py --http
# Test: curl http://localhost:8000/sse
```

### Step 10: Deploy

**Docker:**
```bash
docker build -t your-mcp-server:latest .
docker run -p 8000:8000 your-mcp-server:latest
```

**Kubernetes:**
```bash
# Update deployment.yaml with your image and settings
kubectl apply -f deployment.yaml
kubectl get pods
```

## 📋 Checklist Before Going to Production

- [ ] All example tools removed or replaced
- [ ] `pyproject.toml` updated with your information
- [ ] `SERVER_NAME` configured in `.env` or `config.py`
- [ ] MCP server instructions updated in `mcp_server.py`
- [ ] Custom configuration added (API keys, DB URLs, etc.)
- [ ] Tests written for your tools
- [ ] Docker image built and tested
- [ ] Kubernetes manifests customized
- [ ] Documentation updated with your use case
- [ ] Security review completed
- [ ] Logging configured appropriately
- [ ] Resource limits set for production

## 🎨 Example Use Cases

### Database Query Interface
```python
# tools/database_tools.py
async def query_data(query: str) -> Dict[str, Any]:
    async with db_pool.acquire() as conn:
        results = await conn.fetch(query)
        return {"results": results, "count": len(results)}
```

### ML Inference Server
```python
# tools/ml_tools.py
async def predict(input_text: str) -> Dict[str, Any]:
    prediction = await model.predict(input_text)
    return {
        "input": input_text,
        "prediction": prediction,
        "confidence": model.confidence
    }
```

### Business Logic Engine
```python
# tools/business_rules.py
async def calculate_pricing(order: dict) -> Dict[str, Any]:
    base_price = order['base_price']
    discount = apply_discount_rules(order)
    tax = calculate_tax(base_price - discount)
    return {
        "base_price": base_price,
        "discount": discount,
        "tax": tax,
        "final_price": base_price - discount + tax
    }
```

## 🔍 Architecture Overview

```
Keep These (Infrastructure):
├── mcp_server.py          # Generic MCP server (update tool registrations only)
├── utilities/
│   ├── config.py          # Extend with your settings
│   └── base_tools.py      # Use or extend
├── Dockerfile             # Production ready (use as-is)
├── entrypoint.sh          # Container entrypoint (use as-is)
├── pyproject.toml         # Update metadata
└── .env.example           # Extend with your settings

Replace These (Business Logic):
└── tools/                 # All example tools
    ├── calculator_tools.py   ❌ DELETE
    ├── weather_tools.py      ❌ DELETE
    ├── http_tools.py         ❌ DELETE
    ├── text_tools.py         ❌ DELETE
    └── your_tools.py         ✅ CREATE YOUR OWN
```

## 🤝 Support

- **Documentation**: See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture
- **Examples**: Check `tools/` directory for pattern examples
- **Issues**: The example code shows common patterns for error handling

## 📚 Further Reading

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [ARCHITECTURE.md](ARCHITECTURE.md) - Complete system architecture

---

**Remember**: This is a TEMPLATE. The examples are for learning the pattern, not for production use. Replace them with your actual business logic! 🚀

