"""HTTP client for the public jam band APIs Jambot queries."""

from importlib.metadata import version

import requests

_session: requests.Session | None = None


def get_session() -> requests.Session:
    """Return a process-wide requests.Session with a Jambot User-Agent header."""
    global _session
    if _session is None:
        session = requests.Session()
        session.headers.update({"User-Agent": f"jambot/{version('jambot')}"})
        _session = session
    return _session
