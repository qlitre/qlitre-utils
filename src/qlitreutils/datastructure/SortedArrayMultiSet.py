from array import array
from bisect import bisect_left


class SortedArrayMultiSet:

    def __init__(self, an_iterable: list,
                 array_type: str = 'int'):
        an_iterable.sort()
        if array_type == 'int':
            self.arr = array('i', an_iterable)
        elif array_type == 'float':
            self.arr = array('d', an_iterable)
        elif array_type == 'str':
            self.arr = array('u', an_iterable)

    def __getitem__(self, x: int):
        if x < 0:
            if x < -1 * len(self.arr):
                raise IndexError
        else:
            if x >= len(self.arr):
                raise IndexError
        return self.arr[x]

    def __contains__(self, x) -> bool:
        if len(self.arr) == 0:
            return False
        i = bisect_left(self.arr, x)
        if i >= len(self.arr):
            return False
        if self.arr[i] != x:
            return False
        return True

    def add(self, x):
        idx = bisect_left(self.arr, x)
        self.arr.insert(idx, x)

    def discard(self, x):
        idx = bisect_left(self.arr, x)
        if idx == len(self.arr):
            return
        if self.arr[idx] == x:
            self.arr.pop(idx)

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
