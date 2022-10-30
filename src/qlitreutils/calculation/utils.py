import typing
from collections import deque
import itertools


def moving_average(a_list: list, n: int) -> list:
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


def moving_average_for_loop(a_list: list, n: int) -> list:
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


def get_sum_of_product_pairs(numbers: list) -> int:
    """
    数字のリストを受け取り、ペアの積を合計したものを返す
    ex. [1,2,3]-> 1*2 + 1*3 + 1*3
    1*(2+3) 2*(3)という風に計算する
    """
    remain_total = sum(numbers)
    return_val = 0
    for i, num in enumerate(numbers[:-1]):
        remain_total -= num
        return_val += num * remain_total

    return return_val


def generate_accumulate_in_section(a_list: list, section_length: int) -> typing.Iterable:
    """
    数列の特定の区間の累積和をyieldして返す
    ex.
    a_list=[1,2,3,4,5] section_length=3 => [6,9,12]
    """
    a_list_accumulated = list(itertools.accumulate(a_list))
    for i, number in enumerate(a_list_accumulated):
        if i < section_length - 1:
            continue
        if i == section_length - 1:
            yield number
        else:
            yield number - a_list_accumulated[i - section_length]
