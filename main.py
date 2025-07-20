"""
Mini Pokédex Lite - FastMCP 2.0 Resources Demo (Async Version)

This demo teaches MCP resources by providing a simple Pokédex interface.
It demonstrates:
- Static resource listing with @mcp.resource (async)
- Dynamic resource templates with URI parameters (async)
- External API integration with PokeAPI (async httpx)
- Error handling and JSON responses
- Proper async/await patterns

Usage:
    python main.py

MCP Resources provided:
- poke://pokemon/1 (Bulbasaur)
- poke://pokemon/4 (Charmander) 
- poke://pokemon/7 (Squirtle)
- poke://pokemon/{id} (Any Pokémon by ID)
"""

import httpx
from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError

app = FastMCP(name="mini-pokedex-lite")

# Three starter Pokémon for quick demonstration
STARTERS = {
    "1": "bulbasaur",
    "4": "charmander", 
    "7": "squirtle"
}

@app.resource("poke://starters")
async def list_starters() -> dict:
    """List all starter Pokémon available in this demo."""
    return {
        "starters": [
            {
                "id": pid,
                "name": name.capitalize(),
                "uri": f"poke://pokemon/{pid}"
            }
            for pid, name in STARTERS.items()
        ],
        "total": len(STARTERS)
    }

@app.resource("poke://pokemon/{pokemon_id_or_name}")
async def get_pokemon(pokemon_id_or_name: str) -> dict:
    """
    Get detailed Pokémon information by ID or name.
    
    Examples:
    - poke://pokemon/1 (Bulbasaur)
    - poke://pokemon/25 (Pikachu)
    - poke://pokemon/charizard
    """
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            # Fetch from PokeAPI
            response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}")
            
            if response.status_code == 404:
                raise ResourceError(f"Pokémon with ID/name '{pokemon_id_or_name}' not found")
            elif response.status_code != 200:
                raise ResourceError(f"PokeAPI error: HTTP {response.status_code}")
                
            data = response.json()
            
            return {
                "id": data["id"],
                "name": data["name"].capitalize(),
                "height": data["height"] / 10,  # Convert to meters
                "weight": data["weight"] / 10,  # Convert to kg
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "base_stats": {
                    stat["stat"]["name"]: stat["base_stat"] 
                    for stat in data["stats"]
                },
                "sprite": data["sprites"]["front_default"],
                "api_url": f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}"
            }
            
        except httpx.RequestError as e:
            raise ResourceError(f"Failed to fetch Pokémon data: {str(e)}")
        except (KeyError, ValueError) as e:
            raise ResourceError(f"Error processing Pokémon data: {str(e)}")

@app.resource("poke://types/{type_name}")
async def get_pokemon_by_type(type_name: str) -> dict:
    """
    Get Pokémon of a specific type (bonus resource).
    
    Examples:
    - poke://types/fire
    - poke://types/water
    - poke://types/grass
    """
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            # Fetch type information from PokeAPI
            response = await client.get(f"https://pokeapi.co/api/v2/type/{type_name}")
            
            if response.status_code == 404:
                raise ResourceError(f"Type '{type_name}' not found")
            elif response.status_code != 200:
                raise ResourceError(f"PokeAPI error: HTTP {response.status_code}")
                
            data = response.json()
            
            # Return first 10 Pokémon of this type
            pokemon_list = data["pokemon"][:10]
            
            return {
                "type": type_name.capitalize(),
                "type_id": data["id"],
                "pokemon_count": len(data["pokemon"]),
                "showing": len(pokemon_list),
                "pokemon": [
                    {
                        "name": p["pokemon"]["name"].capitalize(),
                        "uri": f"poke://pokemon/{p['pokemon']['name']}"
                    }
                    for p in pokemon_list
                ]
            }
            
        except httpx.RequestError as e:
            raise ResourceError(f"Failed to fetch type data: {str(e)}")
        except (KeyError, ValueError) as e:
            raise ResourceError(f"Error processing type data: {str(e)}")



if __name__ == "__main__":
    """Run the MCP server."""
    print("🔥 Starting Mini Pokédex Lite MCP Server (Async)...")
    print("📡 Server running on stdio - connect with your MCP client!")
    print("🎯 Try these resources:")
    print("   • poke://starters")
    print("   • poke://pokemon/1")
    print("   • poke://pokemon/pikachu")
    print("   • poke://types/fire")
    app.run(transport="http")
