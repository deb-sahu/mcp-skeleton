"""
MCP Server using Fast MCP.

This module sets up the Model Context Protocol (MCP) server with tool definitions
and configurations. The actual tool implementations are in the tools.py module.
"""

from fastmcp import FastMCP
from tools import (
    get_weather_data,
    calculate_operation,
    fetch_api_data,
    text_analyzer
)

# Initialize FastMCP server
mcp = FastMCP(
    name="Generic MCP Server",
    instructions="A generic skeleton MCP server with sample tools. Customize this for your specific use case."
)


@mcp.tool()
async def get_weather(city: str) -> dict:
    """
    Get weather information for a specific city.
    
    Args:
        city: Name of the city to get weather information for
        
    Returns:
        Weather data including temperature, condition, and more
    """
    return await get_weather_data(city)


@mcp.tool()
async def calculator(operation: str, a: float, b: float) -> dict:
    """
    Perform mathematical operations.
    
    Args:
        operation: Type of operation - 'add', 'subtract', 'multiply', or 'divide'
        a: First number
        b: Second number
        
    Returns:
        Result of the mathematical operation
    """
    return await calculate_operation(operation, a, b)


@mcp.tool()
async def http_request(url: str, method: str = "GET") -> dict:
    """
    Make HTTP requests to external APIs.
    
    Args:
        url: The URL to send the request to
        method: HTTP method (GET or POST), defaults to GET
        
    Returns:
        Response data from the API
    """
    return await fetch_api_data(url, method)


@mcp.tool()
async def analyze_text(text: str) -> dict:
    """
    Analyze text and return various statistics.
    
    Args:
        text: The text to analyze
        
    Returns:
        Text statistics including word count, character count, etc.
    """
    return await text_analyzer(text)


# Entry point for running the server
if __name__ == "__main__":
    # Run the server using the built-in CLI
    # This will start the server with default settings
    mcp.run()
