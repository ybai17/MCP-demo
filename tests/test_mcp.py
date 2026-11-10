# this script file will contain unit tests for the MCP client and model wrapper integration

import json
import asyncio, sys
import pytest
from mcp_client import chat_loop, server_params
from model_wrapper import ModelWrapper
from model import Model, Response, Content
from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client

from horse import SYMBOLI_RUDOLF, GOLD_SHIP, KITASAN_BLACK
from race import ARIMA_KINEN, TEIO_SHO, TENNO_SHO_AUTUMN

CONTENT_NUM_LIMIT = 1
DEBUG_FLAG = True
MODEL = Model(name="LLM")

# needed for anyio backend configuration.
# A plugin that runs outside the async functions and can handle them within an event loop is required
# This is typically handled by the anyio plugin for pytest. Doing this means we can avoid using 
# an @pytest.mark.asyncio decorator on each test function. Pytest basically looks for this variable
# to determine which async backend to use for the tests.
pytestmark = pytest.mark.anyio

@pytest.fixture(scope="session",autouse=True)
def init_before_tests():
    """
    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="AAAAAAAA",
                                            input={},
                                            type="BBBBBBBB",
                                            text="",
                                            id=0)])

    """

    print("Initialized")

@pytest.fixture(scope="session")
async def mcp_client():
    async with Client(stdio_client(server_params("mcp_server.py"))) as client:
                # tool_list = await client.list_tools()
                # tool_names = [tool.name for tool in tool_list.tools]
                # print("\nConnected to server with tools:", tool_names)
        
                yield(client)

# you can either use autouse=True in the fixture to automatically apply it to all tests,
# or include it as an arg for the test functions for them to run it first before executing the test logic
async def test_get_all_horses(mcp_client):

    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="get_all_horses",
                                                input={},
                                                type="tool_use",
                                                text="",
                                                id=0)])

    response = Model.generate_response(MODEL)

    print(response.to_dict())

    content = response.content[0]
    tool_name = content.name
    tool_args = content.input

    # Execute tool call
    result = await mcp_client.call_tool(tool_name, tool_args)
    print(f"[Calling {tool_name} with args {tool_args}]")
    print(f"______________RESULT: {json.loads(result.content[0].text)}")
    assert json.loads(result.content[0].text) == {"data": ["Symboli Rudolf", "Gold Ship", "Kitasan Black"]}

async def test_get_all_races(mcp_client):

    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="get_all_races",
                                                    input={},
                                                    type="tool_use",
                                                    text="",
                                                    id=0)])

    response = Model.generate_response(MODEL)

    print(response.to_dict())

    content = response.content[0]
    tool_name = content.name
    tool_args = content.input


    # Execute tool call
    result = await mcp_client.call_tool(tool_name, tool_args)
    print(f"[Calling {tool_name} with args {tool_args}]")
    # print(f"______________RESULT: {json.loads(result.content[0].text)}")
    assert json.loads(result.content[0].text) == {"data": ["Arima Kinen", "Teio Sho", "Tenno Sho (Autumn)"]}

async def test_get_horse_data(mcp_client):

    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="get_horse_data",
                                                    input={"name": "Symboli Rudolf"},
                                                    type="tool_use",
                                                    text="",
                                                    id=0)])

    response = Model.generate_response(MODEL)

    print(response.to_dict())

    content = response.content[0]
    tool_name = content.name
    tool_args = content.input

    # Execute tool call
    result = await mcp_client.call_tool(tool_name, tool_args)
    print(f"[Calling {tool_name} with args {tool_args}]")
    # print(f"______________RESULT: {json.loads(result.content[0].text)}")
    assert json.loads(result.content[0].text) == {"data": SYMBOLI_RUDOLF.to_dict()}

async def test_get_race_data(mcp_client):

    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="get_race_data",
                                                    input={"name": "Arima Kinen"},
                                                    type="tool_use",
                                                    text="",
                                                    id=0)])

    response = Model.generate_response(MODEL)

    print(response.to_dict())

    content = response.content[0]
    tool_name = content.name
    tool_args = content.input

    # Execute tool call
    result = await mcp_client.call_tool(tool_name, tool_args)
    print(f"[Calling {tool_name} with args {tool_args}]")
    # print(f"______________RESULT: {json.loads(result.content[0].text)}")
    assert json.loads(result.content[0].text) == {"data": ARIMA_KINEN.to_dict()}
    

async def test_get_horse_data_error(mcp_client):

    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="get_horse_data",
                                                    input={"name": "Sirius Symboli"},
                                                    type="tool_use",
                                                    text="",
                                                    id=0)])

    response = Model.generate_response(MODEL)

    print(response.to_dict())

    content = response.content[0]
    tool_name = content.name
    tool_args = content.input

    # Execute tool call
    result = await mcp_client.call_tool(tool_name, tool_args)
    print(f"[Calling {tool_name} with args {tool_args}]")
    print(f"______________RESULT: {json.loads(result.content[0].text)}")
    assert json.loads(result.content[0].text) == {"error": "Horse not found"}
    

async def test_get_race_data_error(mcp_client):

    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="get_race_data",
                                                    input={"name": "Tenno Sho"},
                                                    type="tool_use",
                                                    text="",
                                                    id=0)])

    response = Model.generate_response(MODEL)

    print(response.to_dict())

    content = response.content[0]
    tool_name = content.name
    tool_args = content.input

    result = await mcp_client.call_tool(tool_name, tool_args)
    print(f"[Calling {tool_name} with args {tool_args}]")
    print(f"______________RESULT: {json.loads(result.content[0].text)}")
    assert json.loads(result.content[0].text) == {"error": "Race not found"}

