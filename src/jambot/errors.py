"""Jambot MCP error types."""

from fastmcp.exceptions import ToolError


class JambotError(ToolError):
    """Base error for Jambot MCP failures."""


class JambotValidationError(JambotError):
    """Raised when a tool input fails validation."""
