import json
import os
import pytest

def pytest_configure(config):
    """Register custom test markers to make testing and iterating easier on the developer."""
    config.addinivalue_line("markers", "unit: Unit tests that do not require external dependencies")

@pytest.fixture
def load_fixture():
    def _load_file(filename):
        with open(os.path.join('tests', 'fixtures', filename)) as f:
            return json.load(f)
    return _load_file

@pytest.fixture
def mock_setlists():
    with open(os.path.join('tests', 'fixtures', 'setlists.json')) as f:
        return json.load(f)
