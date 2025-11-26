"""
MCP Skeleton Server - Generic Template
=======================================

🎯 This is a TEMPLATE/SKELETON for building MCP servers.
   Replace the example tools with your own business logic.

This production-ready server provides:
✅ Dual transport modes: stdio (local) + HTTP/SSE (containers)
✅ Clean architecture: Server layer (this file) + Business logic (tools/)
✅ Docker + Kubernetes ready with security best practices
✅ Type-safe configuration with Pydantic

ARCHITECTURE:
-------------
- This file: Generic MCP server infrastructure (keep as-is)
- tools/: Your business logic implementations (replace examples)
- utilities/: Shared configuration and utilities (extend as needed)

EXAMPLE TOOLS (⚠️ REPLACE THESE):
----------------------------------
The imported tools below are DEMONSTRATION examples only:
- calculator_tools: Math operations (simple async function pattern)
- weather_tools: API integration (mock implementation pattern)
- http_tools: HTTP client usage (external API pattern)
- text_tools: Text processing (data transformation pattern)

➡️ Delete or replace these with YOUR domain-specific tools!

TRANSPORT MODES:
----------------
- stdio: Direct MCP client integration (Cursor, VS Code, Claude Desktop)
- HTTP/SSE: Production deployments (Docker, Kubernetes, AKS, cloud)
"""

from fastmcp import FastMCP
import logging
import sys

from utilities.config import settings

# ============================================================================
# Example Tool Imports (⚠️ REPLACE WITH YOUR OWN)
# ============================================================================
# These are DEMONSTRATION tools only. Delete or replace with your business logic:
from tools.weather_tools import get_weather_data      # Example: API integration pattern
from tools.calculator_tools import calculate_operation  # Example: Simple async function
from tools.http_tools import fetch_api_data           # Example: HTTP client usage
from tools.text_tools import text_analyzer            # Example: Data processing

# ✅ Import YOUR tools here instead:
# from tools.database_tools import query_database, insert_record
# from tools.ml_tools import run_inference, get_embeddings
# from tools.business_logic_tools import validate_order, calculate_price
# from tools.api_integration_tools import fetch_external_data

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize MCP server
# Update the 'instructions' below to describe YOUR tools, not the examples
mcp = FastMCP(
    name=settings.server_name,
    instructions=(
        "MCP Skeleton - Template server with example tools (calculator, weather, HTTP, text). "
        "⚠️ REPLACE THIS: Update this description to explain YOUR actual tools and capabilities."
    )
)


# ============================================================================
# MCP Tool Registrations
# ============================================================================
# ⚠️ These are EXAMPLE tool registrations demonstrating the pattern.
#    DELETE or REPLACE them with registrations for YOUR tools.
#
# ARCHITECTURE PRINCIPLE:
# - This section contains thin wrappers that delegate to business logic in tools/
# - Keep these functions minimal - they should only call your tool implementations
# - All actual business logic must live in tools/*.py files, NOT here
# - This keeps the server generic and your business logic modular
#
# PATTERN FOR YOUR TOOLS:
# 1. Import your function: from tools.your_tools import your_function
# 2. Register with @mcp.tool() decorator
# 3. Add docstring (MCP clients will see this)
# 4. Delegate to your implementation: return await your_function(...)
# ============================================================================

# ❌ Example Tool 1: Weather (DEMO - replace with your tool)
@mcp.tool()
async def get_weather(city: str) -> dict:
    """
    [EXAMPLE TOOL] Get weather information for a specific city.
    
    ⚠️ This is a demonstration tool showing API integration pattern.
    Replace with your actual business logic.
    
    Args:
        city: Name of the city to get weather information for
        
    Returns:
        Weather data including temperature, condition, humidity, wind speed, etc.
    """
    return await get_weather_data(city)


# ❌ Example Tool 2: Calculator (DEMO - replace with your tool)
@mcp.tool()
async def calculator(operation: str, a: float, b: float) -> dict:
    """
    [EXAMPLE TOOL] Perform mathematical operations.
    
    ⚠️ This is a demonstration tool showing simple async function pattern.
    Replace with your actual business logic.
    
    Args:
        operation: Type of operation - 'add', 'subtract', 'multiply', or 'divide'
        a: First number
        b: Second number
        
    Returns:
        Result of the mathematical operation with operands
    """
    return await calculate_operation(operation, a, b)


# ❌ Example Tool 3: HTTP Request (DEMO - replace with your tool)
@mcp.tool()
async def http_request(url: str, method: str = "GET") -> dict:
    """
    [EXAMPLE TOOL] Make HTTP requests to external APIs.
    
    ⚠️ This is a demonstration tool showing HTTP client usage pattern.
    Replace with your actual API integration logic.
    
    Args:
        url: The URL to send the request to
        method: HTTP method (GET or POST), defaults to GET
        
    Returns:
        Response data from the API including status code and content
    """
    return await fetch_api_data(url, method)


# ❌ Example Tool 4: Text Analysis (DEMO - replace with your tool)
@mcp.tool()
async def analyze_text(text: str) -> dict:
    """
    [EXAMPLE TOOL] Analyze text and return various statistics.
    
    ⚠️ This is a demonstration tool showing text processing pattern.
    Replace with your actual data processing logic.
    
    Args:
        text: The text to analyze
        
    Returns:
        Text statistics including word count, character count, sentence count,
        average word length, and longest/shortest words
    """
    return await text_analyzer(text)


# ============================================================================
# ✅ Add YOUR Tool Registrations Here
# ============================================================================
# Example template for your tools:
#
# @mcp.tool()
# async def your_tool_name(param1: str, param2: int) -> dict:
#     """
#     Your tool description that MCP clients will see.
#     
#     Args:
#         param1: Description of first parameter
#         param2: Description of second parameter
#         
#     Returns:
#         Description of what your tool returns
#     """
#     # Delegate to your business logic in tools/
#     return await your_function_from_tools(param1, param2)
# ============================================================================


# ============================================================================
# Server Entry Point
# ============================================================================

def main() -> None:
    """Main entry point for the MCP server."""
    logger.info(f"Starting {settings.server_name} v{settings.server_version}...")
    logger.info(f"Log level: {settings.log_level}")
    
    # Support both stdio and HTTP transports
    # Use HTTP if --http flag is provided, otherwise use stdio
    transport = "sse" if "--http" in sys.argv else "stdio"
    
    if transport == "sse":
        logger.info(f"Running in HTTP mode on http://{settings.mcp_server_host}:{settings.mcp_server_port}")
        logger.info(f"MCP endpoint: http://{settings.mcp_server_host}:{settings.mcp_server_port}/sse")
        
        # Monkey patch uvicorn.Config to force host/port binding
        import uvicorn
        original_config_init = uvicorn.Config.__init__
        
        def patched_config_init(self, *args, **kwargs):
            # Force host and port regardless of what was passed
            kwargs['host'] = settings.mcp_server_host
            kwargs['port'] = settings.mcp_server_port
            return original_config_init(self, *args, **kwargs)
        
        uvicorn.Config.__init__ = patched_config_init
        
        mcp.run(transport=transport)
    else:
        logger.info("Running in stdio mode (for direct MCP client integration)")
        mcp.run(transport=transport)


if __name__ == "__main__":
    main()
