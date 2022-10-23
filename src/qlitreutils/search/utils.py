from bisect import bisect_left
from typing import List


def get_nearest_value_in_list(an_iterable: List[int], target: int) -> int:
    """リストの中から最も近い値を探索して返す"""
    an_iterable.sort()
    index = bisect_left(an_iterable, target)
    if index == 0:
        return an_iterable[0]
    if index == len(an_iterable):
        return an_iterable[-1]
    a = target - an_iterable[index - 1]
    b = an_iterable[index] - target
    if a < b:
        return an_iterable[index - 1]
    else:
        return an_iterable[index]
