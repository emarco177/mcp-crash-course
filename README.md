# Mini Pokédex Lite - FastMCP 2.0 Async Resources Demo

A simple yet comprehensive example demonstrating **async MCP Resources** using FastMCP 2.0 and the Pokémon API.

## 🎯 What This Demo Teaches

This project demonstrates key MCP concepts using the **KISS principle** with modern async patterns:

- **Async Static Resources** - Fixed data endpoints (`poke://starters`, `poke://info`)
- **Async Dynamic Resource Templates** - Parameterized URIs (`poke://pokemon/{id}`, `poke://types/{type}`)
- **Async External API Integration** - Non-blocking HTTP requests with `httpx`
- **Error Handling** - Proper `ResourceError` usage in async context
- **JSON Responses** - Structured data return with async processing

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- An MCP-compatible client (Claude Desktop, MCP Inspector, etc.)

### Installation

```bash
# Clone and setup
git clone <this-repo>
cd mcp-crash-course

# Install dependencies
uv sync
# or: pip install -e .
```

### Running the Server

```bash
python main.py
```

The server runs on **stdio** and waits for MCP client connections.

## 📚 Available Resources

| Resource URI | Description | Example |
|--------------|-------------|---------|
| `poke://starters` | List the 3 starter Pokémon | Static async data |
| `poke://pokemon/{id}` | Get any Pokémon by ID/name | `poke://pokemon/25` |
| `poke://types/{type}` | Get Pokémon by type (first 10) | `poke://types/fire` |
| `poke://info` | API information & usage | Static metadata |

## 🔍 Example Usage

### With MCP Inspector

```bash
# Install MCP Inspector
npm install -g @modelcontextprotocol/inspector

# Connect to your server
mcp-inspector python main.py
```

### Testing Resources

1. **List Starters**: `poke://starters`
   ```json
   {
     "starters": [
       {"id": "1", "name": "Bulbasaur", "uri": "poke://pokemon/1"},
       {"id": "4", "name": "Charmander", "uri": "poke://pokemon/4"},
       {"id": "7", "name": "Squirtle", "uri": "poke://pokemon/7"}
     ],
     "total": 3
   }
   ```

2. **Get Pokémon Details**: `poke://pokemon/pikachu`
   ```json
   {
     "id": 25,
     "name": "Pikachu",
     "height": 0.4,
     "weight": 6.0,
     "types": ["electric"],
     "abilities": ["static", "lightning-rod"],
     "base_stats": {
       "hp": 35,
       "attack": 55,
       "defense": 40,
       "special-attack": 50,
       "special-defense": 50,
       "speed": 90
     },
     "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
   }
   ```

3. **Get Pokémon by Type**: `poke://types/fire`
   ```json
   {
     "type": "Fire",
     "type_id": 10,
     "pokemon_count": 73,
     "showing": 10,
     "pokemon": [
       {"name": "Charmander", "uri": "poke://pokemon/charmander"},
       {"name": "Charmeleon", "uri": "poke://pokemon/charmeleon"},
       {"name": "Charizard", "uri": "poke://pokemon/charizard"}
     ]
   }
   ```

## 🏗️ Code Structure

### FastMCP 2.0 Async Features Used

```python
import httpx
from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError

app = FastMCP(name="mini-pokedex-lite")

# Async static resource
@app.resource("poke://starters")
async def list_starters() -> dict:
    return {"starters": [...]}

# Async dynamic resource template
@app.resource("poke://pokemon/{pokemon_id}")
async def get_pokemon(pokemon_id: str) -> dict:
    # Access pokemon_id parameter from URI
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        
        if response.status_code == 404:
            raise ResourceError(f"Pokémon '{pokemon_id}' not found")
        
        return process_pokemon_data(response.json())
```

### Key Async Patterns

- **Async Resource Decorator**: `@app.resource(uri)` with `async def` - Non-blocking data exposure
- **URI Templates**: `{parameter}` syntax for dynamic resources
- **Async HTTP Client**: `httpx.AsyncClient` for non-blocking API calls
- **Context Managers**: `async with` for proper resource cleanup
- **Error Handling**: Use `ResourceError` for client-friendly messages in async context
- **Type Hints**: Help with IDE support and async function documentation
- **Docstrings**: Become resource descriptions automatically

## 🎓 Learning Goals

After studying this demo, you'll understand:

1. **Resource vs Tools**: Resources are read-only data, tools perform actions
2. **Async Resources**: Non-blocking resource functions with `async def`
3. **URI Design**: How to structure resource identifiers
4. **Template Parameters**: Dynamic resource creation with async processing
5. **Async HTTP**: Using `httpx` for non-blocking API calls
6. **External APIs**: Integrating third-party data sources asynchronously
7. **Error Patterns**: Proper exception handling in async MCP context

## 🔧 Extending the Demo

Try adding these async features:

- **More Resources**: `poke://moves/{move}`, `poke://regions/{region}`
- **Async Caching**: Store API responses with async cache libraries (aioredis)
- **Connection Pooling**: Reuse httpx connections across requests
- **Concurrent Requests**: Fetch multiple Pokémon data simultaneously
- **Rate Limiting**: Implement async rate limiting for PokeAPI
- **Background Tasks**: Cache warming or data preloading
- **Streaming**: Large data streaming with async generators
- **Database Integration**: Async database queries with SQLAlchemy/Tortoise

## 📖 Related Resources

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [PokéAPI Documentation](https://pokeapi.co/docs/v2)

## 🏷️ Tags

`#mcp` `#fastmcp` `#async` `#resources` `#api` `#demo` `#pokemon` `#tutorial` `#httpx` `#asyncio`
