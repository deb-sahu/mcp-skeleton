"""
Tests for Weather Tools
========================

Example test cases showing how to test API integration patterns.
Replace these tests with tests for YOUR API integrations.
"""

import pytest
from tools.weather_tools import get_weather_data


@pytest.mark.asyncio
async def test_get_weather_data_returns_structure():
    """Test weather data returns correct structure."""
    result = await get_weather_data("London")
    
    assert "city" in result
    assert "temperature" in result
    assert "condition" in result
    assert "humidity" in result
    assert "wind_speed" in result
    assert "message" in result


@pytest.mark.asyncio
async def test_get_weather_data_city_name():
    """Test weather data includes requested city."""
    city = "Tokyo"
    result = await get_weather_data(city)
    assert result["city"] == city


@pytest.mark.asyncio
async def test_get_weather_data_mock_values():
    """Test mock data returns expected types."""
    result = await get_weather_data("Paris")
    
    assert isinstance(result["temperature"], (int, float))
    assert isinstance(result["condition"], str)
    assert isinstance(result["humidity"], (int, float))
    assert isinstance(result["wind_speed"], (int, float))

