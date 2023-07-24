#!/usr/bin/env python3
''' '''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    st_in = (page - 1) * page_size
    end_in = page * page_size
    return st_in, end_in
