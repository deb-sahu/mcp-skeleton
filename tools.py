"""
Tools implementation module.

This module contains the actual logic and implementations for tools
used by the MCP server. Separate the business logic from the MCP
server configuration for better maintainability.
"""

import httpx
from typing import Dict, Any


async def get_weather_data(city: str) -> Dict[str, Any]:
    """
    Fetch weather data for a given city.
    
    This is a sample implementation that would typically call a weather API.
    Replace with your actual API integration.
    
    Args:
        city: Name of the city to get weather for
        
    Returns:
        Dictionary containing weather information
    """
    # Example implementation - replace with actual API call
    # For demonstration, returning mock data
    return {
        "city": city,
        "temperature": 72,
        "condition": "Sunny",
        "humidity": 45,
        "wind_speed": 10,
        "message": "This is sample data. Integrate with a real weather API."
    }


async def calculate_operation(operation: str, a: float, b: float) -> Dict[str, Any]:
    """
    Perform a mathematical operation.
    
    Args:
        operation: Type of operation (add, subtract, multiply, divide)
        a: First number
        b: Second number
        
    Returns:
        Dictionary containing the result
        
    Raises:
        ValueError: If operation is not supported or division by zero
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None
    }
    
    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}. Choose from: {list(operations.keys())}")
    
    result = operations[operation](a, b)
    
    if result is None:
        raise ValueError("Division by zero is not allowed")
    
    return {
        "operation": operation,
        "operand_a": a,
        "operand_b": b,
        "result": result
    }


async def fetch_api_data(url: str, method: str = "GET", headers: Dict[str, str] = None) -> Dict[str, Any]:
    """
    Make an HTTP request to an external API.
    
    Args:
        url: The URL to fetch data from
        method: HTTP method (GET, POST, etc.)
        headers: Optional HTTP headers
        
    Returns:
        Dictionary containing the response data
        
    Raises:
        Exception: If the request fails
    """
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers or {})
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers or {})
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            
            return {
                "status_code": response.status_code,
                "url": str(response.url),
                "data": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text
            }
        except Exception as e:
            return {
                "error": str(e),
                "url": url,
                "method": method
            }


async def text_analyzer(text: str) -> Dict[str, Any]:
    """
    Analyze text and return statistics.
    
    Args:
        text: The text to analyze
        
    Returns:
        Dictionary containing text statistics
    """
    words = text.split()
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", ""))
    sentences = text.count(".") + text.count("!") + text.count("?")
    
    return {
        "text_length": characters,
        "characters_no_spaces": characters_no_spaces,
        "word_count": len(words),
        "sentence_count": max(sentences, 1),
        "average_word_length": round(characters_no_spaces / max(len(words), 1), 2),
        "longest_word": max(words, key=len) if words else "",
        "shortest_word": min(words, key=len) if words else ""
    }
