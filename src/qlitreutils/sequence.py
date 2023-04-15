"""
生成系のユーティリティ
"""

from functools import lru_cache
from collections import deque


@lru_cache(maxsize=None)
def gen_seq_within_sum_limit_and_length(remain: int, depth: int, length: int) -> list:
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
        for j in gen_seq_within_sum_limit_and_length(remain - i, depth + 1, length):
            ret.append([i] + j)
    return ret


def gen_increasing_seq(length: int, limit: int) -> list:
    ret = []
    que = deque()
    for i in range(1, limit + 1):
        que.append(([i], 1))

    while que:
        al, depth = que.popleft()
        if depth == length:
            ret.append(al)
        else:
            last = al[-1]
            for i in range(last, limit + 1):
                que.append((al + [i], depth + 1))

    return ret