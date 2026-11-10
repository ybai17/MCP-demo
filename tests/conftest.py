import pytest
from mcp_client import server_params
from model import Content, Model, Response
from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client

CONTENT_NUM_LIMIT = 1
DEBUG_FLAG = True
MODEL = Model(name="LLM")

# needed for anyio backend configuration.
# A plugin that runs outside the async functions and can handle them within an event loop is required
# This is typically handled by the anyio plugin for pytest. Pytest looks for this fixture to determine which async backend to use for the tests.
@pytest.fixture(scope="session")
def anyio_backend():
    # session-scoped async fixtures need a session-scoped backend
    return "asyncio"


@pytest.fixture(scope="session", autouse=False)
def test_init():

    """
    Model.generate_response = lambda self, max_tokens=1000, messages=[{}], tools=[]: Response([Content(name="get_all_horses",
                                        input={},
                                        type="tool_use",
                                        text="",
                                        id=0)])

    """

    pass
