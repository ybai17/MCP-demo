# reference: https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#python

import logging
from typing import Any

import httpx2
from mcp.server import MCPServer

logger = logging.getLogger(__name__)

mcp = MCPServer("horse_mcp")

logger.info("Starting horse MCP server")

# Constants
API_BASE_URL = "http://127.0.0.1:5000"
USER_AGENT = "horse_app/1.0"

async def make_request(url: str) -> dict[str, Any] | None:
    """Make request to the horse API with proper error handling.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        dict[str, Any] | None: The JSON response as a dictionary if successful, None otherwise.
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}

    async with httpx2.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx2.HTTPError as e:
            logger.error("Error making request to %s: %s", url, e)
            return response.json() if response is not None else None

# Tools

@mcp.tool()
async def get_horse_data(name: str) -> dict[str, Any] | None:
    """Fetch all attribute data for a horse from the API.

    Args:
        name (str): The name of the horse to fetch data for.

    Returns:
        dict[str, Any] | None: The JSON response as a dictionary if successful, None otherwise.
    """
    url = f"{API_BASE_URL}/horse/{name}"

    return await make_request(url)

@mcp.tool()
async def get_race_data(name: str) -> dict[str, Any] | None:
    """Fetch all attribute data for a race from the API.

    Args:
        name (str): The name of the race to fetch data for.

    Returns:
        dict[str, Any] | None: The JSON response as a dictionary if successful, None otherwise.
    """

    url = f"{API_BASE_URL}/race/{name}"

    return await make_request(url)

@mcp.tool()
async def get_all_horses() -> dict[str, Any] | None:
    """Fetch a list of all horses from the API.

    Returns:
        dict[str, Any] | None: The JSON response as a dictionary if successful, None otherwise.
    """
    url = f"{API_BASE_URL}/horse/"

    return await make_request(url)

@mcp.tool()
async def get_all_races() -> dict[str, Any] | None:
    """Fetch a list of all races from the API.

    Returns:
        dict[str, Any] | None: The JSON response as a dictionary if successful, None otherwise.
    """
    url = f"{API_BASE_URL}/race/"

    return await make_request(url)

logger.info("Horse MCP server is running")

if __name__ == "__main__":

    # ensures the MCP server runs with the specified transport layer (stdio in this case)
    mcp.run(transport="stdio")

    # todo: look into how to run MCP server as web service (transport over HTTP/HTTPS)
