#!/usr/bin/env python3
"""
Our Module
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    random_float = random.random() * (max_delay - 0) + 0
    await asyncio.sleep(random_float)
    return random_float
