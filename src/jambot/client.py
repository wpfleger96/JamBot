"""HTTP client for the public jam band APIs Jambot queries."""

from contextlib import asynccontextmanager
from importlib.metadata import version

import httpx

_client: httpx.AsyncClient | None = None


def get_client() -> httpx.AsyncClient:
    """Return the active httpx.AsyncClient.

    Raises:
        RuntimeError: if called while the server lifespan is not active.
    """
    if _client is None:
        raise RuntimeError(
            "HTTP client is not initialized; the server lifespan must be active."
        )
    return _client


@asynccontextmanager
async def lifespan(app):
    """FastMCP lifespan: open the shared httpx.AsyncClient for the server's lifetime."""
    global _client
    async with httpx.AsyncClient(
        headers={"User-Agent": f"jambot/{version('jambot')}"},
        timeout=30.0,
    ) as client:
        _client = client
        try:
            yield
        finally:
            _client = None
