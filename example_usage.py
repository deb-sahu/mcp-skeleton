"""
Example usage of the MCP server.

This script demonstrates how to connect to and use the MCP server
with a client.
"""

import asyncio
from fastmcp import FastMCP, Client


async def main():
    """Demonstrate MCP server usage."""
    
    # Option 1: Import and use the server directly
    print("=" * 60)
    print("Example 1: Using Server Directly (In-Process)")
    print("=" * 60)
    
    from mcp_server import mcp
    
    # Access tools directly from the server
    tools = await mcp.get_tools()
    print(f"\nAvailable tools: {list(tools.keys())}")
    
    # Option 2: Connect as a client (for remote server)
    print("\n" + "=" * 60)
    print("Example 2: Using Client to Connect")
    print("=" * 60)
    
    # When connecting to a running server, use Client with the server instance
    async with Client(mcp) as client:
        # List available tools
        tools_list = await client.list_tools()
        print(f"\nAvailable tools via client:")
        for tool in tools_list:
            print(f"  - {tool.name}: {tool.description}")
        
        # Call the calculator tool
        print("\n" + "-" * 60)
        print("Calling calculator tool (add 15 + 27):")
        result = await client.call_tool(
            "calculator",
            arguments={"operation": "add", "a": 15, "b": 27}
        )
        print(f"Result: {result.content}")
        
        # Call the text analyzer tool
        print("\n" + "-" * 60)
        print("Calling text analyzer tool:")
        result = await client.call_tool(
            "analyze_text",
            arguments={"text": "The quick brown fox jumps over the lazy dog."}
        )
        print(f"Result: {result.content}")
        
        # Call the weather tool
        print("\n" + "-" * 60)
        print("Calling weather tool:")
        result = await client.call_tool(
            "get_weather",
            arguments={"city": "San Francisco"}
        )
        print(f"Result: {result.content}")
    
    print("\n" + "=" * 60)
    print("Examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
