"""
生成系のユーティリティ
"""

from functools import lru_cache
from collections import deque


@lru_cache(maxsize=None)
def generate_sequences_within_sum_limit_and_length(remain: int, depth: int, length: int) -> list:
    """
        深さ優先探索を使用して、長さlengthで足してremain以下の数列を生成する。
        depthは1を指定する。
        Args:
            remain (int): 生成する数列の合計がremain以下である必要がある。
            depth (int): 現在の深さ。再帰的に呼び出されるたびに、depthは1ずつ増加する。
            length (int): 生成する数列の長さ。

        Returns:
            List[List[int]]: 長さlengthで足してremain以下の数列のリスト。

        Example:
            remain=5,length=3
            [[1, 1, 3], [1, 2, 2], [1, 3, 1], [2, 1, 2], [2, 2, 1], [3, 1, 1]]
        """
    if remain <= 0:
        return []
    if depth == 0:
        return []
    if depth == length:
        return [[i] for i in range(1, remain + 1)]

    ret = []
    for i in range(1, remain + 1):
        for j in generate_sequences_within_sum_limit_and_length(remain - i, depth + 1, length):
            ret.append([i] + j)
    return ret


def generate_lunlun_numbers(limit: int) -> list:
    """
    ルンルン数を小さい順に生成して返す。
    ルンルン数=>正の整数X を(leading zeroなしで)十進数表記した際に、隣り合うどの2つの桁の値についても、差の絶対値が1以下
    ex:
    1234
    1
    334
    """
    ret = []
    # 1桁のルンルン数をキューに入れる
    que = deque(range(1, 10))

    while len(ret) < limit:
        cur_num = que.popleft()
        ret.append(cur_num)
        # 最後の桁の数字
        last_digit = cur_num % 10
        # 最後の桁から1を引いた数
        if last_digit > 0:
            que.append(cur_num * 10 + last_digit - 1)
        # 最後の桁と同じ数
        que.append(cur_num * 10 + last_digit)
        # 最後の桁に1を足した数
        if last_digit < 9:
            que.append(cur_num * 10 + last_digit + 1)
    ret.sort()
    return ret


print(generate_sequences_within_sum_limit_and_length(5, 1, 3))
