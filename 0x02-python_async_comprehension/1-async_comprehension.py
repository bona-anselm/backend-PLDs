#!/usr/bin/env python3
"""
Async Comprehension Module
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator
async def async_comprehension() -> List[float]:
    """Async comprehension Function"""
    return [a async for a in async_generator()]
