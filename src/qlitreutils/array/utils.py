from typing import List, Tuple, Union
from collections import deque


def get_connected_value_list(a_list: List[Tuple[Union[int, str], ...]],
                             start_value: Union[int, str]
                             ) -> List[Union[int, str]]:
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

