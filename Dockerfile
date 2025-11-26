# MCP Skeleton Server
# Production Dockerfile for AKS deployment

FROM python:3.12-slim

# Set build arguments
ARG POETRY_VERSION=1.7.1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd --uid 10001 -md /home/mcpuser mcpuser

# Install poetry
RUN pip install --upgrade pip && \
    pip install poetry==${POETRY_VERSION}

# Configure poetry to not create virtual env (using container isolation)
RUN poetry config virtualenvs.create false

# Set working directory
WORKDIR /app

# Copy dependency files
COPY --chown=mcpuser:mcpuser pyproject.toml poetry.lock* ./

# Install dependencies as root (for system packages)
RUN poetry install --no-root --only main --no-interaction --no-ansi

# Copy application code with folder structure
COPY --chown=mcpuser:mcpuser mcp_server.py /app/
COPY --chown=mcpuser:mcpuser tools/ /app/tools/
COPY --chown=mcpuser:mcpuser utilities/ /app/utilities/
COPY --chown=mcpuser:mcpuser README.md /app/
COPY --chown=mcpuser:mcpuser .env.example /app/.env

# Copy and set permissions for entrypoint script
COPY --chown=mcpuser:mcpuser entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Switch to non-root user
USER mcpuser

# Expose HTTP port for MCP server
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/sse || exit 1

# Run the MCP server using entrypoint script
CMD ["/app/entrypoint.sh"]
