"""
Tests for Calculator Tools
===========================

Example test cases showing how to test your tool implementations.
Replace these tests with tests for YOUR business logic.
"""

import pytest
from tools.calculator_tools import calculate_operation


@pytest.mark.asyncio
async def test_add_operation():
    """Test addition operation."""
    result = await calculate_operation("add", 5, 3)
    assert result["operation"] == "add"
    assert result["operand_a"] == 5
    assert result["operand_b"] == 3
    assert result["result"] == 8


@pytest.mark.asyncio
async def test_subtract_operation():
    """Test subtraction operation."""
    result = await calculate_operation("subtract", 10, 4)
    assert result["operation"] == "subtract"
    assert result["result"] == 6


@pytest.mark.asyncio
async def test_multiply_operation():
    """Test multiplication operation."""
    result = await calculate_operation("multiply", 6, 7)
    assert result["operation"] == "multiply"
    assert result["result"] == 42


@pytest.mark.asyncio
async def test_divide_operation():
    """Test division operation."""
    result = await calculate_operation("divide", 15, 3)
    assert result["operation"] == "divide"
    assert result["result"] == 5


@pytest.mark.asyncio
async def test_divide_by_zero():
    """Test division by zero raises error."""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        await calculate_operation("divide", 10, 0)


@pytest.mark.asyncio
async def test_invalid_operation():
    """Test invalid operation raises error."""
    with pytest.raises(ValueError, match="Unsupported operation"):
        await calculate_operation("modulo", 10, 3)

