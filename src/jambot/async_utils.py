"""Utilities for async operations with the synchronous requests client."""

import asyncio
import logging
from typing import Any, Callable

logger = logging.getLogger(__name__)


async def safe_execute_async(func: Callable[[], Any], operation_name: str) -> Any:
    """Execute a synchronous function asynchronously in a thread pool.

    This wrapper allows synchronous `requests` calls to be executed without
    blocking the event loop, using `asyncio.to_thread`.

    Args:
        func: A callable that performs the synchronous operation
        operation_name: A descriptive name for the operation (used in error logs)

    Returns:
        The result of the synchronous operation

    Raises:
        Re-raises any exception from the operation.
    """
    try:
        return await asyncio.to_thread(func)
    except Exception as e:
        logger.error(f"Failed to execute {operation_name}: {e}")
        raise
