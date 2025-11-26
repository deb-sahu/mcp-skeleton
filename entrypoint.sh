#!/bin/sh
# Entrypoint script for MCP Skeleton Server

set -e

echo "Starting MCP Skeleton Server..."

# Run the MCP server (host/port are set via env vars and monkey-patched in mcp_server.py)
exec python mcp_server.py --http
