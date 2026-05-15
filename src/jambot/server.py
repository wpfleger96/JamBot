"""Jambot MCP Server main module."""

import json
from functools import wraps
from importlib.metadata import version
from typing import Any, Awaitable, Callable, List, Optional

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from pydantic import BaseModel

from jambot import resources, utils
from jambot.constants import RESOURCE_MODEL_MAP, RESOURCE_TYPES, SUPPORTED_BANDS_MAP

INSTRUCTIONS = f"""
Jambot v{version('jambot')}

REQUIRED READING:
- You are Jambot MCP server. You query for jam band resources in the following ways:
    1. All data for a given resource type and band code using the `get_resources` tool.
    2. A specific resource for a given resource type and band code by ID using the `get_resource` tool.
    3. A list of resources for a given resource type and band code by query using the `query_resources` tool.
- Each supported band has a unique band code. Supported Bands and their band codes are documented at the `docs://supported_bands` resource.
- All resource types are supported for all bands. A list of supported Resource Types are documented at the `docs://resource_types` resource.
- To view the schema for a specific resource type, read the `docs://schemas/{{resource_type}}` resource.
"""

mcp = FastMCP(
    name="jambot",
    instructions=INSTRUCTIONS,
)


def tool_error_boundary(
    func: Callable[..., Awaitable[Any]],
) -> Callable[..., Awaitable[Any]]:
    """Convert common tool failures into ToolError so FastMCP sets isError=true."""

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        try:
            return await func(*args, **kwargs)
        except ToolError:
            raise
        except Exception as exc:
            response = getattr(exc, "response", None)
            if response is not None:
                message = response.text
            else:
                message = str(exc)
            raise ToolError(message) from exc

    return wrapper


"""
MCP Server Documentation
"""


@mcp.resource("docs://resource_types")
def get_resource_types() -> str:
    return json.dumps(RESOURCE_TYPES, indent=2)


@mcp.resource("docs://schemas/{resource_type}")
def get_schema(resource_type: str) -> str:
    return json.dumps(utils.model_to_schema(RESOURCE_MODEL_MAP[resource_type]), indent=2)


@mcp.resource("docs://supported_bands")
def get_supported_bands() -> str:
    result = []
    for band in SUPPORTED_BANDS_MAP:
        result.append({"name": SUPPORTED_BANDS_MAP[band]["name"], "band_code": band})
    return json.dumps(result, indent=2)


"""
MCP Server Tools
"""


@mcp.tool()
@tool_error_boundary
async def get_resources(
    *,
    band: str,
    resource_type: str,
    format: Optional[str] = "json",
    order_by: Optional[str] = None,
    direction: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[BaseModel]:
    """Get all resources for a given band and resource type.

    Args:
        band (str): The band code to get resources for.
        resource_type (str): The resource type to get.
        format (str): The format to get the resource in. Defaults to `json`. Supported formats are `json` and `html`.
        order_by (str): The column to order the resources by. Defaults to None.
        direction (str): The direction to order the resources by, either "asc" or "desc". Defaults to "asc".
        limit (int): The maximum number of resources to return. Defaults to None.
    """
    return await resources.list_resources(
        band=band,
        resource_type=resource_type,
        format=format,
        order_by=order_by,
        direction=direction,
        limit=limit,
    )


@mcp.tool()
@tool_error_boundary
async def get_resource(
    *,
    id: str,
    band: str,
    resource_type: str,
    format: Optional[str] = "json",
) -> BaseModel:
    """Get a specific resource for a given band and resource type by its ID.

    Args:
        id (str): The ID of the resource to get.
        band (str): The band code to get resources for.
        resource_type (str): The resource type to get.
        format (str): The format to get the resource in. Defaults to "json".
    """
    return await resources.show_resource(
        id=id,
        band=band,
        resource_type=resource_type,
        format=format,
    )


@mcp.tool()
@tool_error_boundary
async def query_resources(
    *,
    query_column: str,
    query_value: str,
    band: str,
    resource_type: str,
    format: Optional[str] = "json",
) -> List[BaseModel]:
    """Query resources for a given band and resource type by a query column and query value.

    Args:
        query_column (str): The column to query on.
        query_value (str): The value to query on.
        band (str): The band code to query on.
        resource_type (str): The resource type to query on.
        format (str): The format to get the resource in. Defaults to "json".
    """
    return await resources.query_resources_by_column(
        query_column=query_column,
        query_value=query_value,
        band=band,
        resource_type=resource_type,
        format=format,
    )
