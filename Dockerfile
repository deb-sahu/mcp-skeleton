# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY mcp_server.py .
COPY tools.py .

# Expose default MCP server port (if using HTTP transport)
EXPOSE 8000

# Run the MCP server
# Note: By default, the server runs with STDIO transport
# To use HTTP transport, pass additional arguments like:
# CMD ["python", "mcp_server.py", "--transport", "sse"]
CMD ["python", "mcp_server.py"]
