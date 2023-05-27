from array import array
from bisect import bisect_left
from typing import List, Union, Literal


class SortedArraySet:

    def __init__(self, an_iterable: Union[List[int], List[float], List[str]],
                 array_type=Literal['int', 'float', 'str']):
        an_iterable.sort()

        if array_type == 'int':
            self.arr = array('i', an_iterable)
        elif array_type == 'float':
            self.arr = array('d', an_iterable)
        elif array_type == 'str':
            self.arr = array('u', an_iterable)

        self.a_set = set(an_iterable)

    def add(self, x):
        if x not in self.a_set:
            idx = bisect_left(self.arr, x)
            self.arr.insert(idx, x)
            self.a_set.add(x)

    def discard(self, x):
        if x in self.a_set:
            idx = bisect_left(self.arr, x)
            self.arr.pop(idx)
            self.a_set.discard(x)

    def lt(self, x):
        idx = bisect_left(self.arr, x)
        for i in range(idx, -1, -1):
            if self.arr[i] < x:
                return self.arr[i]
        return None

    def le(self, x):
        idx = bisect_left(self.arr, x)
        for i in range(idx, -1, -1):
            if self.arr[i] <= x:
                return self.arr[i]
        return None

    def gt(self, x):
        idx = bisect_left(self.arr, x)
        for i in range(idx, len(self.arr)):
            if self.arr[i] > x:
                return self.arr[i]
        return None

    def ge(self, x):
        idx = bisect_left(self.arr, x)
        for i in range(idx, len(self.arr)):
            if self.arr[i] >= x:
                return self.arr[i]
        return None
