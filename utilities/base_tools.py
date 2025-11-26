"""
Base tools module for MCP Skeleton.

Provides base classes and utilities for creating consistent tool responses
across all MCP tools in the server.
"""

from typing import Dict, Any, List, Optional, TypeVar, Generic
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T')


class ToolResponse(BaseModel, Generic[T]):
    """
    Standard response format for all MCP tools.
    
    Provides consistent structure across all tool responses with:
    - success: Boolean indicating if operation succeeded
    - data: The actual response data (typed)
    - error: Optional error message if operation failed
    """
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed = True


class BaseTools:
    """
    Base class for all tool implementations.
    
    Provides common utilities and patterns for tool development:
    - Structured logging
    - Consistent error handling
    - Standard response formatting
    """
    
    def __init__(self, service_name: str):
        """
        Initialize base tools.
        
        Args:
            service_name: Name of the service/tool for logging purposes
        """
        self.service_name = service_name
        self.logger = logging.getLogger(f"{__name__}.{service_name}")
    
    def success_response(self, data: Any) -> Dict[str, Any]:
        """
        Create a success response.
        
        Args:
            data: The response data
            
        Returns:
            Dictionary with success=True and data
        """
        return {
            "success": True,
            "data": data,
            "error": None
        }
    
    def error_response(self, error: str, data: Any = None) -> Dict[str, Any]:
        """
        Create an error response.
        
        Args:
            error: Error message
            data: Optional partial data
            
        Returns:
            Dictionary with success=False and error message
        """
        self.logger.error(f"{self.service_name} error: {error}")
        return {
            "success": False,
            "data": data,
            "error": error
        }
