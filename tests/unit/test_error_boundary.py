"""MCP boundary tests: verify Jambot failures set isError=true."""

from typing import cast
from unittest.mock import AsyncMock, patch

import pytest
from fastmcp.client import Client
from mcp.types import TextContent

from jambot.errors import JambotError
from jambot.server import mcp


def _text(content: list) -> str:
    return cast(TextContent, content[0]).text


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.server
async def test_resource_layer_error_sets_is_error() -> None:
    """JambotError from the resource layer should surface as an MCP tool error."""
    with patch(
        "jambot.server.resources.list_resources",
        side_effect=JambotError("upstream API exploded"),
    ):
        async with Client(mcp) as client:
            result = await client.call_tool_mcp(
                "get_resources",
                {"band": "goose", "resource_type": "setlists"},
            )

    assert result.isError is True
    assert result.content
    assert "upstream API exploded" in _text(result.content)


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.server
async def test_validation_error_sets_is_error() -> None:
    """Validation failures from the resource layer should surface as MCP tool errors."""
    async with Client(mcp) as client:
        result = await client.call_tool_mcp(
            "get_resources",
            {"band": "not-a-band", "resource_type": "setlists"},
        )

    assert result.isError is True
    assert result.content
    assert "Invalid band" in _text(result.content)


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.server
async def test_unexpected_exception_sets_is_error() -> None:
    """Non-ToolError exceptions should still be converted to MCP tool errors."""
    with patch(
        "jambot.server.resources.list_resources",
        side_effect=RuntimeError("kaboom"),
    ):
        async with Client(mcp) as client:
            result = await client.call_tool_mcp(
                "get_resources",
                {"band": "goose", "resource_type": "setlists"},
            )

    assert result.isError is True
    assert "kaboom" in _text(result.content)


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.server
async def test_successful_call_sets_is_error_false() -> None:
    """Successful tool calls should not set isError."""
    mocked = AsyncMock(return_value=[])
    with patch("jambot.server.resources.list_resources", mocked):
        async with Client(mcp) as client:
            result = await client.call_tool_mcp(
                "get_resources",
                {"band": "goose", "resource_type": "setlists"},
            )

    assert result.isError is False
