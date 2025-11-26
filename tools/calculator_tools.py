"""
Calculator tools for MCP Skeleton.

Provides mathematical calculation capabilities.
"""

from typing import Dict, Any


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
