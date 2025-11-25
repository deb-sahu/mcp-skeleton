# MCP Server Skeleton

A generic skeleton for building Model Context Protocol (MCP) servers using Fast MCP. This template provides a clean separation between server configuration and tool implementation, making it easy to customize for your specific use case.

## 🏗️ Project Structure

```
mcp-skeleton/
├── mcp_server.py       # MCP server setup and tool declarations
├── tools.py            # Actual tool implementations and business logic
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration for deployment
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 📋 Features

- **Clean Architecture**: Separation of concerns between MCP server configuration and tool logic
- **Sample Tools**: Pre-configured example tools demonstrating common patterns:
  - Weather data fetching
  - Mathematical calculator
  - HTTP request handling
  - Text analysis
- **Docker Support**: Ready-to-use Dockerfile for containerized deployment
- **Type Hints**: Full type annotations for better IDE support and code quality
- **Async/Await**: Modern Python async patterns for efficient I/O operations

## 🚀 Quick Start

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/deb-sahu/mcp-skeleton.git
   cd mcp-skeleton
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   python mcp_server.py
   ```

   The server will start and be ready to accept MCP connections.

### Docker Deployment

#### Using Docker Compose (Recommended)

1. **Copy the environment file:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. **Start the service:**
   ```bash
   docker-compose up -d
   ```

3. **View logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Stop the service:**
   ```bash
   docker-compose down
   ```

#### Using Docker directly

1. **Build the Docker image:**
   ```bash
   docker build -t mcp-server .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 mcp-server
   ```

   The server will be available at `http://localhost:8000`

## 🔧 Customization

### Adding New Tools

1. **Implement the tool logic in `tools.py`:**
   ```python
   async def my_custom_tool(param1: str, param2: int) -> dict:
       """Your tool implementation."""
       # Your logic here
       return {"result": "success"}
   ```

2. **Register the tool in `mcp_server.py`:**
   ```python
   @mcp.tool()
   async def my_tool(param1: str, param2: int) -> dict:
       """
       Description of what your tool does.
       
       Args:
           param1: Description of param1
           param2: Description of param2
       """
       return await my_custom_tool(param1, param2)
   ```

### Modifying Server Configuration

Edit the `FastMCP` initialization in `mcp_server.py`:

```python
mcp = FastMCP(
    name="Your Server Name",
    instructions="Custom instructions for your server",
    # Add more configuration options as needed
)
```

## 📚 Available Tools

### 1. Weather Tool
Get weather information for a city.
```python
await get_weather(city="London")
```

### 2. Calculator
Perform mathematical operations.
```python
await calculator(operation="add", a=5, b=3)
```

### 3. HTTP Request
Make HTTP requests to external APIs.
```python
await http_request(url="https://api.example.com", method="GET")
```

### 4. Text Analyzer
Analyze text and get statistics.
```python
await analyze_text(text="Your text here")
```

## 🧪 Testing

Test the server by connecting with an MCP client or using the built-in testing tools.

```python
from fastmcp import Client

async with Client("http://localhost:8000") as client:
    result = await client.call_tool("calculator", {"operation": "add", "a": 5, "b": 3})
    print(result)
```

## 🔐 Environment Variables

Create a `.env` file for environment-specific configuration:

```env
# Example environment variables
API_KEY=your_api_key_here
LOG_LEVEL=INFO
PORT=8000
```

## 📦 Dependencies

- **fastmcp**: Fast MCP framework for building MCP servers
- **httpx**: Modern HTTP client for API requests
- **python-dotenv**: Environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [Fast MCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Python Async/Await Guide](https://docs.python.org/3/library/asyncio.html)

## 💡 Tips

- Keep tool implementations in `tools.py` focused on business logic
- Use `mcp_server.py` only for MCP-specific configuration and tool registration
- Add comprehensive docstrings to all tools for better discoverability
- Use type hints for better IDE support and error catching
- Implement proper error handling in your tool functions
- Consider adding logging for debugging and monitoring

## 🆘 Support

For issues, questions, or contributions, please open an issue on the GitHub repository.
