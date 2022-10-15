from typing import List
from collections import deque


def moving_average(a_list: List, n: int) -> List:
    """移動平均リストを返す"""
    results = []
    a_list = deque(a_list)
    tmp = deque()
    while a_list:
        tmp.append(a_list.popleft())
        if len(tmp) == n:
            _sum = sum(tmp)
            avg = _sum / n
            results.append(avg)
            tmp.popleft()

    return results


def moving_average_for_loop(a_list: List, n: int) -> List:
    """移動平均リストを返す　for loop版"""
    results = []
    for i, item in enumerate(a_list, start=1):
        if i < n:
            continue
        tmp = a_list[i - n:i]
        _sum = sum(tmp)
        avg = _sum / n
        results.append(avg)
    return results
