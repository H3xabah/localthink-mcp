"""Thread-pool parallel runner for batch and scan tools.

Uses ThreadPoolExecutor rather than asyncio to avoid nested-event-loop conflicts
with FastMCP's own async runtime. generate() calls are I/O-bound (HTTP to Ollama)
and release the GIL, so threads give genuine concurrency.
"""
from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable

_MAX_WORKERS = int(os.environ.get("LOCALTHINK_MAX_CONCURRENCY", "4"))


def run_batch(
    callables: list[Callable[[], str]],
    max_workers: int = _MAX_WORKERS,
) -> list[str]:
    """Run zero-argument callables in parallel; return results in original order.

    Any callable that raises an exception gets an error string in its slot.
    """
    if not callables:
        return []
    n = len(callables)
    results: list[str] = [""] * n
    workers = min(max_workers, n)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        future_to_idx = {pool.submit(fn): i for i, fn in enumerate(callables)}
        for future in as_completed(future_to_idx):
            idx = future_to_idx[future]
            try:
                results[idx] = future.result()
            except Exception as exc:
                results[idx] = f"[localthink] thread error: {exc}"
    return results
