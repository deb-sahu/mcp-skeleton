"""
HTTP request tools for MCP Skeleton.

Provides capabilities to make HTTP requests to external APIs.
"""

import httpx
from typing import Dict, Any


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
            
            # Try to parse JSON if content-type suggests it
            data = response.text
            if response.headers.get("content-type", "").startswith("application/json"):
                try:
                    data = response.json()
                except ValueError:
                    # If JSON parsing fails, fall back to text
                    data = response.text
            
            return {
                "status_code": response.status_code,
                "url": str(response.url),
                "data": data
            }
        except Exception as e:
            return {
                "error": str(e),
                "url": url,
                "method": method
            }
