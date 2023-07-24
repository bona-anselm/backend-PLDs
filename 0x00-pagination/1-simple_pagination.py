#!/usr/bin/env python3
"""
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    st_in = (page - 1) * page_size
    end_in = page * page_size
    return st_in, end_in

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and > 0 'should_err '
        assert isinstance(page_size, int)  and > 0 'should_err '
        start_index, end_index = index_range(page, page_size)
        if len(self.__dataset) < end_index
        if start_index > range    
