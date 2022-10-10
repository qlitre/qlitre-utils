from typing import List


def moving_average(a_list: List, n: int) -> List:
    results = []
    tmp = []
    while a_list:
        tmp.append(a_list.pop(0))
        if len(tmp) == n:
            _sum = sum(tmp)
            avg = _sum / n
            results.append(avg)
            tmp.pop(0)

    return results


def moving_average_for_loop(a_list: List, n: int) -> List:
    results = []
    for i, item in enumerate(a_list, start=1):
        if i < n:
            continue
        tmp = a_list[i - n:i]
        _sum = sum(tmp)
        avg = _sum / n
        results.append(avg)
    return results
