"""Unit tests for jambot.utils."""

import pytest

from jambot import utils
from jambot.models.setlists import Setlist


@pytest.mark.unit
@pytest.mark.utils
def test_model_to_schema_returns_field_types():
    schema = utils.model_to_schema(Setlist)
    assert isinstance(schema, dict)
    assert "showdate" in schema
    assert "show_id" in schema
