# reference: https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client

import asyncio
import sys
from pathlib import Path
from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp_types import TextContent

from model_wrapper import ModelWrapper
from model import Model

from dotenv import load_dotenv

load_dotenv()

MODEL = Model(name="LLM")
MODEL_WRAPPER = ModelWrapper(model=MODEL)
DEBUG_FLAG = True

# note that this is tied to the running environment being in Powershell, with uv being the program used to run the script.
# e.g. uv run mcp_server.py

# Another later option would be to have the user directly call something like "uv run client.py path/to/server.py"

def server_params(server_script_path: str) -> StdioServerParameters:
    """Describes the subprocess that runs an MCP server under the MCP client.

    Args:
        server_script_path (str): The path to the server script to be executed (.py).

    Returns:
        StdioServerParameters: The parameters describing the subprocess, as a StdioServerParameters object.
    """


    # use Path class to handle potential cases where VS code can't exactly resolve the relative path of the mcp_server
    # script file correctly, by providing an absolute path
    path = Path(server_script_path)

    if not path.is_absolute():
        path = (Path(__file__).parent / path).resolve()
    if path.suffix != ".py":
        raise ValueError("Server script must have a .py suffix")


    if path.suffix == ".py":
        command = "uv"
    else:
        raise ValueError("Script must be a .py file")

    return StdioServerParameters(command=command, args=["run", str(path)])

# Functions for processing queries and handling tool calls

async def process_query(client: Client, query: str) -> str:
    """Process a query using the given model and available tools.

    Args:
        client (Client): The MCP client instance to use for processing the query.
        query (str): The query string to process.

    Returns:
        str: The response from the tool as a string.
    """

    # this will store the message history for the entire duration of the conversation with the LLM
    messages = [
        {
            "role": "user",
            "content": query
        }
    ]

    tool_list = await client.list_tools()

    available_tool_list = [{
        "name": tool.name,
        "description": tool.description,
        "input_schema": tool.input_schema
    } for tool in tool_list.tools]

    # need to get simulated response from fake model. Need to figure out what the response actually would look like.
    # test using actual model at home, extract output, and then simulate something similar.

    # or we can use monkey patching to do this

    # initial LLM API call telling the model what tools are available to it
    response = MODEL_WRAPPER.send_prompt(MODEL, max_tokens=1000, messages=messages, tools=available_tool_list)

    final_text = []
    tool_results = []

    for content in response.content:
        if content.type == "text":
            final_text.append(content.text)
        elif content.type == "tool_use":
            tool_name = content.name
            tool_args = content.input

            if DEBUG_FLAG:
                print(f"___CLIENT: Calling tool '{tool_name}' with args {tool_args}")

            # Execute tool call
            result = await client.call_tool(tool_name, tool_args)
            final_text.append(f"[Calling {tool_name} with args {tool_args}]")

            tool_results.append({
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": "\n".join(
                    block.text
                    for block in result.content
                    if isinstance(block, TextContent)                    
                ),
                "is_error": result.is_error
            })

    # get next response from LLM
    if tool_results:
        messages.append({"role": "assistant", "content": response.content[0].to_dict()})
        messages.append({"role": "user", "content": tool_results})

        # get next response from model
        response = MODEL_WRAPPER.send_prompt(MODEL, max_tokens=1000, messages=messages, tools=available_tool_list)

        for content in response.content:
            if content.type == "text":
                final_text.append(content.text)

    if DEBUG_FLAG:
        print("===================")
        print("Messages:", messages)
        print("-------------------")
        print("Final text so far:", "\n".join(final_text))
        print("-------------------")
        print(tool_results)
        print("===================")

    return "\n".join(final_text)

async def chat_loop(client: Client) -> None:
    """Run an interactive chat loop with the MCP client.

    Args:
        client (Client): The MCP client instance to use for the chat loop.
    """

    print("MCP client started. Enter queries or type 'quit' to exit.")

    while True:
        try:
            query = (await asyncio.to_thread(input, "\nQuery: ")).strip()

        except EOFError:
            print("\nExiting chat loop.")
            break

        if query.lower() == 'quit':
            break

        try:
            response = await process_query(client, query)
            print("\n" + response)
        except Exception as e:
            print(f"\nError: {e}")

async def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python mcp_client.py <server_script_path>")
        sys.exit(1)

    async with Client(stdio_client(server_params(sys.argv[1]))) as client:
        tool_list = await client.list_tools()
        tool_names = [tool.name for tool in tool_list.tools]
        print("\nConnected to server with tools:", tool_names)

        await chat_loop(client)

if __name__ == "__main__":
    asyncio.run(main())
