"""
配列操作のユーティリティ
"""

from collections import deque


def move_zeros_deque(a_list: list):
    """数列の0を右に寄せる　deque版"""
    ret = deque()
    for item in reversed(a_list):
        if item == 0:
            ret.append(0)
        else:
            ret.appendleft(item)

    return list(ret)


def move_zeros_basic(a_list):
    """数列の0を右に寄せる　標準版"""
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list


def generate_round_trip_value(a_list: list, count: int):
    """
    配列を往復させて値をyieldして返す
    """
    a_list = deque(a_list)
    n = -1
    first = a_list[0]
    last = a_list[-1]
    for i in range(count):
        ret = a_list[0]
        if ret == first:
            n = -1
        if ret == last:
            n = 1

        a_list.rotate(n)

        yield ret


def get_difference_sequence(a_list: list) -> list:
    """階差数列を返す"""
    n = len(a_list)
    if n < 2:
        raise ValueError("要素は２つ必要")
    return [a_list[i + 1] - a_list[i] for i in range(n - 1)]


def count_inversion(a_list: list) -> int:
    """転倒数を返す"""
    count = 0
    for i in range(len(a_list) - 1):
        for j in range(i + 1, len(a_list)):
            if a_list[i] > a_list[j]:
                count += 1
    return count
