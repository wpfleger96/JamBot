from importlib.metadata import version
from typing import Optional, List
import requests
import json
from urllib.parse import urlencode
from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP

from jambot import utils
from jambot.constants import SUPPORTED_BANDS_MAP, RESOURCE_TYPES, FORMATS, RESOURCE_MODEL_MAP

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

server = FastMCP(
    name="jambot",
    instructions=INSTRUCTIONS
)


"""
MCP Server Documentation
"""
@server.resource("docs://resource_types")
def get_resource_types() -> str:
    return json.dumps(RESOURCE_TYPES, indent=2)

@server.resource("docs://schemas/{resource_type}")
def get_schema(resource_type: str) -> str:
    return json.dumps(utils.model_to_schema(RESOURCE_MODEL_MAP[resource_type]), indent=2)

@server.resource("docs://supported_bands")
def get_supported_bands() -> str:
    result = []
    for band in SUPPORTED_BANDS_MAP:
        result.append({
            "name": SUPPORTED_BANDS_MAP[band]['name'],
            "band_code": band
        })
    return json.dumps(result, indent=2)


"""
MCP Server Tools
"""
@server.tool("get_resources")
def get_resources(*,
                 band: str,
                 resource_type: str,
                 format: Optional[str] = "json",
                 order_by: Optional[str] = None,
                 direction: Optional[str] = None,
                 limit: Optional[int] = None) -> List[BaseModel]:
    """Get all resources for a given band and resource type.

    Args:
        band (str): The band code to get resources for.
        resource_type (str): The resource type to get.
        format (str): The format to get the resource in. Defaults to `json`. Supported formats are `json` and `html`.
        order_by (str): The column to order the resources by. Defaults to None.
        direction (str): The direction to order the resources by, either "asc" or "desc". Defaults to "asc".
        limit (int): The maximum number of resources to return. Defaults to None.
    """
    utils.validate_band(band)
    utils.validate_resource_type(resource_type)
    utils.validate_format(format)
    if order_by:
        utils.validate_order_by(order_by, resource_type)
    if direction:
        utils.validate_direction(direction)

    url = f"{SUPPORTED_BANDS_MAP[band]['url']}/{resource_type}.{format}"

    params = {k: v for k, v in {
        'order_by': order_by,
        'direction': direction,
        'limit': limit
    }.items() if v is not None}

    if params:
        url += f"?{urlencode(params)}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        response_data = response.json()
        model_class = RESOURCE_MODEL_MAP[resource_type]
        return [model_class(**item) for item in response_data["data"]]
    except Exception as e:
        raise ValueError(f"Error getting resource for {band} and {resource_type}: {e}.")
    
@server.tool("get_resource")
def get_resource(*,
                 id: str,
                 band: str,
                 resource_type: str,
                 format: Optional[str] = "json") -> BaseModel:
    """Get a specific resource for a given band and resource type by its ID.

    Args:
        id (str): The ID of the resource to get.
        band (str): The band code to get resources for.
        resource_type (str): The resource type to get.
        format (str): The format to get the resource in. Defaults to "json".
    """
    utils.validate_band(band)
    utils.validate_resource_type(resource_type)
    utils.validate_format(format)

    url = f"{SUPPORTED_BANDS_MAP[band]['url']}/{resource_type}/{id}.{format}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        response_data = response.json()
        model_class = RESOURCE_MODEL_MAP[resource_type]
        return model_class(**response_data)
    except Exception as e:
        raise ValueError(f"Error getting resource for {band} and {resource_type}: {e}.")

@server.tool("query_resources")
def query_resources(*,
                    query_column: str,
                    query_value: str,
                    band: str,
                    resource_type: str,
                    format: Optional[str] = "json") -> List[BaseModel]:
    """Query resources for a given band and resource type by a query column and query value.

    Args:
        query_column (str): The column to query on.
        query_value (str): The value to query on.
        band (str): The band code to query on.
        resource_type (str): The resource type to query on.
        format (str): The format to get the resource in. Defaults to "json".
    """
    utils.validate_band(band)
    utils.validate_resource_type(resource_type)
    utils.validate_format(format)

    url = f"{SUPPORTED_BANDS_MAP[band]['url']}/{resource_type}/{query_column}/{query_value}.{format}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        response_data = response.json()
        model_class = RESOURCE_MODEL_MAP[resource_type]
        return [model_class(**item) for item in response_data["data"]]
    except Exception as e:
        raise ValueError(f"Error querying resources for {band} and {resource_type}: {e}.")
    