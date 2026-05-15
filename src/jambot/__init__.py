"""Jambot MCP Server.

A server that exposes public jam band APIs to LLMs as MCP tools and resources.
"""

from .server import mcp

__all__ = ["mcp", "main"]


def main():
    """Entry point for the Jambot MCP Server."""
    from .__main__ import main as _main

    return _main()
