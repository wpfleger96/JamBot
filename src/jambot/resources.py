"""Async data layer for fetching jam band resources from public APIs."""

import logging
from typing import List, Optional

from pydantic import BaseModel

from jambot import validation
from jambot.client import get_client
from jambot.constants import RESOURCE_MODEL_MAP, SUPPORTED_BANDS_MAP
from jambot.errors import JambotError

logger = logging.getLogger(__name__)


async def list_resources(
    *,
    band: str,
    resource_type: str,
    format: str = "json",
    order_by: Optional[str] = None,
    direction: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[BaseModel]:
    """Fetch all resources for a band+resource_type."""
    validation.validate_band(band)
    validation.validate_resource_type(resource_type)
    validation.validate_format(format)
    if order_by:
        validation.validate_order_by(order_by, resource_type)
    if direction:
        validation.validate_direction(direction)

    url = f"{SUPPORTED_BANDS_MAP[band]['url']}/{resource_type}.{format}"
    params = {
        k: v
        for k, v in {"order_by": order_by, "direction": direction, "limit": limit}.items()
        if v is not None
    }

    client = get_client()
    try:
        response = await client.get(url, params=params)
        response.raise_for_status()
        response_data = response.json()
        model_class = RESOURCE_MODEL_MAP[resource_type]
        return [model_class(**item) for item in response_data["data"]]
    except Exception as e:
        raise JambotError(
            f"Error getting resources for {band} and {resource_type}: {e}."
        ) from e


async def show_resource(
    *,
    id: str,
    band: str,
    resource_type: str,
    format: str = "json",
) -> BaseModel:
    """Fetch a single resource by ID."""
    validation.validate_band(band)
    validation.validate_resource_type(resource_type)
    validation.validate_format(format)

    url = f"{SUPPORTED_BANDS_MAP[band]['url']}/{resource_type}/{id}.{format}"
    client = get_client()
    try:
        response = await client.get(url)
        response.raise_for_status()
        response_data = response.json()
        model_class = RESOURCE_MODEL_MAP[resource_type]
        return model_class(**response_data)
    except Exception as e:
        raise JambotError(
            f"Error getting resource for {band} and {resource_type}: {e}."
        ) from e


async def query_resources_by_column(
    *,
    query_column: str,
    query_value: str,
    band: str,
    resource_type: str,
    format: str = "json",
) -> List[BaseModel]:
    """Query resources by an arbitrary column/value pair."""
    validation.validate_band(band)
    validation.validate_resource_type(resource_type)
    validation.validate_format(format)

    url = (
        f"{SUPPORTED_BANDS_MAP[band]['url']}/{resource_type}/"
        f"{query_column}/{query_value}.{format}"
    )
    client = get_client()
    try:
        response = await client.get(url)
        response.raise_for_status()
        response_data = response.json()
        model_class = RESOURCE_MODEL_MAP[resource_type]
        return [model_class(**item) for item in response_data["data"]]
    except Exception as e:
        raise JambotError(
            f"Error querying resources for {band} and {resource_type}: {e}."
        ) from e
