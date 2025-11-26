"""
Configuration management for MCP Skeleton Server.

Uses pydantic-settings for type-safe configuration with environment variables.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    All settings can be overridden by setting environment variables.
    Example: export SERVER_NAME="My Custom MCP Server"
    """
    
    # Server Configuration
    server_name: str = "MCP Skeleton Server"
    server_version: str = "0.1.0"
    log_level: str = "INFO"
    
    # MCP Server Configuration (for HTTP/SSE transport)
    mcp_server_host: str = "0.0.0.0"
    mcp_server_port: int = 8000
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
