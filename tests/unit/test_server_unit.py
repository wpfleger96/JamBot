import pytest

from jambot import mcp


@pytest.mark.unit
@pytest.mark.server
def test_mcp():
    """Test that the server initializes correctly."""
    assert mcp.name == "jambot"
