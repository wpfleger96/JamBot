"""Unit tests for the async resource data layer."""

from unittest.mock import MagicMock, patch

import pytest

from jambot import resources
from jambot.errors import JambotError
from jambot.models.setlists import Setlist


def _mock_response(json_data, status_code: int = 200):
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = json_data
    response.raise_for_status = MagicMock()
    return response


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_list_resources_parses_setlists(mock_setlists):
    payload = {"data": mock_setlists}
    response = _mock_response(payload)
    session = MagicMock()
    session.get.return_value = response

    with patch("jambot.resources.get_session", return_value=session):
        result = await resources.list_resources(
            band="goose", resource_type="setlists", format="json"
        )

    assert isinstance(result, list)
    assert len(result) == len(mock_setlists)
    assert all(isinstance(item, Setlist) for item in result)
    session.get.assert_called_once()
    called_url = session.get.call_args.args[0]
    assert called_url.startswith("https://elgoose.net/api/v2/setlists.json")


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
async def test_list_resources_http_error_wrapped(mock_setlists):
    response = _mock_response({"data": mock_setlists}, status_code=500)
    response.raise_for_status.side_effect = RuntimeError("HTTP 500")
    session = MagicMock()
    session.get.return_value = response

    with patch("jambot.resources.get_session", return_value=session):
        with pytest.raises(JambotError) as excinfo:
            await resources.list_resources(
                band="goose", resource_type="setlists", format="json"
            )
    assert "HTTP 500" in str(excinfo.value)


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_list_resources_builds_query_string():
    response = _mock_response({"data": []})
    session = MagicMock()
    session.get.return_value = response

    with patch("jambot.resources.get_session", return_value=session):
        await resources.list_resources(
            band="um",
            resource_type="shows",
            format="json",
            order_by="showdate",
            direction="desc",
            limit=5,
        )

    called_url = session.get.call_args.args[0]
    assert called_url.startswith("https://allthings.umphreys.com/api/v2/shows.json?")
    assert "order_by=showdate" in called_url
    assert "direction=desc" in called_url
    assert "limit=5" in called_url


@pytest.mark.asyncio
@pytest.mark.unit
@pytest.mark.resources
async def test_query_resources_builds_path(mock_setlists):
    response = _mock_response({"data": mock_setlists})
    session = MagicMock()
    session.get.return_value = response

    with patch("jambot.resources.get_session", return_value=session):
        await resources.query_resources_by_column(
            query_column="showyear",
            query_value="2024",
            band="goose",
            resource_type="setlists",
            format="json",
        )

    called_url = session.get.call_args.args[0]
    assert called_url == (
        "https://elgoose.net/api/v2/setlists/showyear/2024.json"
    )
