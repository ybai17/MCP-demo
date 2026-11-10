import asyncio, sys, os, json
import anyio

from mcp import Client, ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv

load_dotenv(".env")

# Reference for the code: 
# https://py.sdk.modelcontextprotocol.io/client/#whats-on-a-connected-client

# Note that StdioServerParameters can take either an actual URL or a command to run a local server script
# URL if transport layer is over HTTP/HTTPS and MCP server is running as a web service
# Example: mcp_server_params = StdioServerParameters(command="http://localhost:8000")
# Command if running a local server script
# Example: mcp_server_params = StdioServerParameters(command="uv", args=["run", "mcp_server.py"]) AKA "uv run mcp_server.py"

mcp_server_params = StdioServerParameters(command="uv", args=["run", "mcp_server.py"])

async def main() -> None:
    async with Client(mcp_server_params) as client:

        # "get_horse_data" is content.name, and the dict is content.input containing the expected tool call arguments
        result = await client.call_tool("get_all_horses", {})
        #print(result)

        print(result.model_dump_json())

        #print(client.server_info)
        #print(client.server_capabilities)
        #print(client.protocol_version)
        #print(client.instructions)


if __name__ == "__main__":
    anyio.run(main)

"""
class MCPClient:
    def __init__(self):
        self.session = None
        self.exit_stack = AsyncExitStack()
        self.http_session = None

    async def connet_to_server(self, server_script_path: str):

        # Determine runtime (Python/Node.js)
        command = "python" if server_script_path.endswith(".py") else "node"

        server_params = StdioServerParameters(command=command, args=[server_script_path])

"""
