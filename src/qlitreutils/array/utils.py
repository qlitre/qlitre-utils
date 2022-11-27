"""
配列操作のユーティリティ
"""

from collections import deque, defaultdict


def get_connected_value_list(a_list: list, start_value) -> list:
    """
    タプルのリストを受け取り、繋がっている要素をリストにして返す
    例えばある地点からスタートして、どこまでたどり着けるか調べる
    warning:割と速度に不安がある。技術試験などでは辞書かして、get_can_visitを使った方がよい
    :param a_list ex.[(1, 2), (1, 3), (3, 6), (4, 5)]
    :param start_value 最初に調べる値、例えばスタート地点
    """
    ret = [start_value]
    checked = set()
    checked.add(start_value)
    que = deque([start_value])
    while que:
        check_val = que.popleft()
        for item in a_list:
            if check_val not in item:
                continue
            for elm in item:
                if elm in checked:
                    continue
                else:
                    ret.append(elm)
                    que.append(elm)
                    checked.add(elm)
    return ret


def count_can_visit(start, connected: dict, include_start: bool = False) -> int:
    """
    ある地点を起点に訪れることのできる場所の数を返す
    :param start:開始する数値、connectedのキーを指定
    :param connected:{0:[1,3,4],1:[2,3,4]...}
    :param include_start:開始地点を数に含めるか
    """
    checked = set()
    checked.add(start)
    cnt = 1 if include_start else 0
    que = deque()
    que.append(start)
    while que:
        now_place = que.popleft()
        for to_place in connected[now_place]:
            if to_place in checked:
                continue
            cnt += 1
            que.append(to_place)
            checked.add(to_place)
    return cnt


def get_can_visit(start, connected: dict, include_start: bool = False) -> list:
    """
    ある地点を起点に訪れることのできる場所をリストにして返す
    :param start:開始する数値、connectedのキーを指定
    :param connected:{0:[1,3,4],1:[2,3,4]...}
    :param include_start:開始地点を数に含めるか

    """
    checked = set()
    checked.add(start)
    ret = [start] if include_start else []
    que = deque()
    que.append(start)
    while que:
        now_place = que.popleft()
        for to_place in connected[now_place]:
            if to_place in checked:
                continue
            ret.append(to_place)
            que.append(to_place)
            checked.add(to_place)
    return ret


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
