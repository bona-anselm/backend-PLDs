#!/usr/bin/env python3
""""
My Module Documented
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay:int) -> float:
    """
    My Function
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time = elapsed_time / n
    return total_time
