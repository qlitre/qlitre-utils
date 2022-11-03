from collections import deque


def get_connected_value_list(a_list: list, start_value) -> list:
    """
    タプルのリストを受け取り、繋がっている要素をリストにして返す
    例えばある地点からスタートして、どこまでたどり着けるか調べる
    :param a_list ex.[(1, 2), (1, 3), (3, 6), (4, 5)]
    :param start_value 最初に調べる値、例えばスタート地点
    """
    check_remains = deque([start_value])
    return_values = []
    while True:
        check_value = check_remains.popleft()
        for item in a_list:
            if check_value not in item:
                continue
            for elm in item:
                if elm not in return_values:
                    return_values.append(elm)
                    check_remains.append(elm)
        if not check_remains:
            break
    return return_values


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
