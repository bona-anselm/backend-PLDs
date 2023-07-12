#!/usr/bin/env python3
"""
Measure Runtime Module
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
async def measure_runtime() -> float:
    """Measure time for 4 concurrent execution"""
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.time()
    lag = end - start
    return lag
