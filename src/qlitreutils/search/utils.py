from bisect import bisect_left


def get_nearest_value_in_list(an_iterable: list, target: int) -> int:
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


def binary_search(a_list: list, target: int) -> bool:
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == target:
            return True
        else:
            if target < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


def binary_search_w_bisect(an_iterable: list, target: int) -> bool:
    index = bisect_left(an_iterable, target)
    if index >= len(an_iterable):
        return False
    if an_iterable[index] == target:
        return True
    return False
