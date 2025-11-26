"""
Tools Package - MCP Skeleton Server
====================================

ARCHITECTURE PRINCIPLE:
This package demonstrates separation of concerns by keeping business logic
outside the server layer. The MCP server (mcp_server.py) only handles:
- Tool registration via @mcp.tool() decorators
- Request/response orchestration
- Transport management (stdio/HTTP)

All business logic resides here in modular, reusable tool implementations.

SKELETON PATTERN:
This is a GENERIC template - not a weather-specific or text-specific server.
Replace the example tools below with your own domain-specific implementations.

Example Tool Structure:
-----------------------
Tool 1 (calculator_tools.py):
    Purpose: Mathematical operations
    Pattern: Async function with typed parameters
    Registration: Imported and wrapped in mcp_server.py @mcp.tool() decorator
    
Tool 2 (weather_tools.py):
    Purpose: External API integration (mock example)
    Pattern: Async function returning structured data
    Registration: Imported and wrapped in mcp_server.py @mcp.tool() decorator
    
Tool 3 (http_tools.py):
    Purpose: HTTP request capabilities
    Pattern: Async function with httpx client
    Registration: Imported and wrapped in mcp_server.py @mcp.tool() decorator
    
Tool 4 (text_tools.py):
    Purpose: Text processing utilities
    Pattern: Async function with analysis logic
    Registration: Imported and wrapped in mcp_server.py @mcp.tool() decorator

HOW TO ADD YOUR OWN TOOLS:
---------------------------
1. Create a new file: tools/your_tool.py
   Example: tools/database_tools.py, tools/api_tools.py
   
2. Implement async function with business logic:
   ```python
   async def your_tool_function(param: str) -> Dict[str, Any]:
       # Your business logic here
       return {"result": "data"}
   ```
   
3. Export it here in __init__.py:
   Add to imports and __all__ list
   
4. Register in mcp_server.py:
   ```python
   @mcp.tool()
   async def your_tool(param: str) -> dict:
       '''Tool description for MCP clients'''
       return await your_tool_function(param)
   ```

This pattern keeps server code clean and business logic modular, testable,
and reusable across different MCP server implementations.
"""

# Example Tool Implementations (Replace with your own)
from .calculator_tools import calculate_operation  # Tool 1: Math operations
from .weather_tools import get_weather_data        # Tool 2: API integration
from .http_tools import fetch_api_data             # Tool 3: HTTP requests
from .text_tools import text_analyzer              # Tool 4: Text processing

# Export all tool functions for server registration
__all__ = [
    'calculate_operation',  # Tool 1
    'get_weather_data',     # Tool 2
    'fetch_api_data',       # Tool 3
    'text_analyzer',        # Tool 4
]
