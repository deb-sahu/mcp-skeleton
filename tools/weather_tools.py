"""
Weather tools for MCP Skeleton.

Provides weather information capabilities with mock data.
"""

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
