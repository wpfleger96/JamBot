"""Unit tests for the async resource data layer."""

from typing import Callable
from unittest.mock import patch

import httpx
import pytest

from jambot import resources
from jambot.errors import JambotError
from jambot.models.setlists import Setlist


def _client(handler: Callable[[httpx.Request], httpx.Response]) -> httpx.AsyncClient:
    """Build an httpx.AsyncClient backed by a mock transport."""
    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_list_resources_parses_setlists(mock_setlists):
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"data": mock_setlists})

    with patch("jambot.resources.get_client", return_value=_client(handler)):
        result = await resources.list_resources(
            band="goose", resource_type="setlists", format="json"
        )

    assert isinstance(result, list)
    assert len(result) == len(mock_setlists)
    assert all(isinstance(item, Setlist) for item in result)
    assert len(seen) == 1
    assert str(seen[0].url).startswith("https://elgoose.net/api/v2/setlists.json")


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_list_resources_invalid_band_raises_validation():
    with pytest.raises(JambotError) as excinfo:
        await resources.list_resources(
            band="invalid", resource_type="setlists", format="json"
        )
    assert "Invalid band" in str(excinfo.value)


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_list_resources_http_error_wrapped():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(500, text="server error")

    with patch("jambot.resources.get_client", return_value=_client(handler)):
        with pytest.raises(JambotError) as excinfo:
            await resources.list_resources(
                band="goose", resource_type="setlists", format="json"
            )
    assert "500" in str(excinfo.value)


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_list_resources_builds_query_string():
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"data": []})

    with patch("jambot.resources.get_client", return_value=_client(handler)):
        await resources.list_resources(
            band="um",
            resource_type="shows",
            format="json",
            order_by="showdate",
            direction="desc",
            limit=5,
        )

    url = seen[0].url
    assert str(url).startswith("https://allthings.umphreys.com/api/v2/shows.json?")
    assert url.params.get("order_by") == "showdate"
    assert url.params.get("direction") == "desc"
    assert url.params.get("limit") == "5"


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_query_resources_builds_path(mock_setlists):
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"data": mock_setlists})

    with patch("jambot.resources.get_client", return_value=_client(handler)):
        await resources.query_resources_by_column(
            query_column="showyear",
            query_value="2024",
            band="goose",
            resource_type="setlists",
            format="json",
        )

    assert str(seen[0].url) == (
        "https://elgoose.net/api/v2/setlists/showyear/2024.json"
    )
