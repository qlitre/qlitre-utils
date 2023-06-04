from array import array
from bisect import bisect_left


class SortedArraySet:

    def __init__(self, an_iterable: list,
                 array_type: str = 'int'):
        self.a_set = set(an_iterable)

        an_iterable = list(self.a_set)
        an_iterable.sort()
        if array_type == 'int':
            self.arr = array('i', an_iterable)
        elif array_type == 'float':
            self.arr = array('d', an_iterable)
        elif array_type == 'str':
            self.arr = array('u', an_iterable)

        self.size = len(self.arr)

    def __str__(self) -> str:
        s = str(list(self.arr))
        return "{" + s[1: len(s) - 1] + "}"

    def __iter__(self):
        for i in self.arr:
            yield i

    def __len__(self) -> int:
        return self.size

    def add(self, x) -> None:
        if x not in self.a_set:
            idx = bisect_left(self.arr, x)
            self.arr.insert(idx, x)
            self.a_set.add(x)
            self.size += 1

    def discard(self, x) -> None:
        if x in self.a_set:
            idx = bisect_left(self.arr, x)
            self.arr.pop(idx)
            self.a_set.discard(x)
            self.size -= 1

    def lt(self, x):
        idx = bisect_left(self.arr, x)
        if idx == self.size:
            return self.arr[-1]
        for i in range(idx, -1, -1):
            if self.arr[i] < x:
                return self.arr[i]
        return None

    def le(self, x):
        idx = bisect_left(self.arr, x)
        if idx == self.size:
            return self.arr[-1]
        for i in range(idx, -1, -1):
            if self.arr[i] <= x:
                return self.arr[i]
        return None

    def gt(self, x):
        idx = bisect_left(self.arr, x)
        for i in range(idx, self.size):
            if self.arr[i] > x:
                return self.arr[i]
        return None

    def ge(self, x):
        idx = bisect_left(self.arr, x)
        for i in range(idx, self.size):
            if self.arr[i] >= x:
                return self.arr[i]
        return None
