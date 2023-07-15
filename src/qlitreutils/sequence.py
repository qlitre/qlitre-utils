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


def find_all_groupings(idx, group, n, group_count) -> list:
    """
    指定された総数nとグループの総数を元に、
    深さ優先探索（DFS）を用いて全ての可能なグループ分けを返す。
    条件：
    各indexは1つのグループに入る
    各グループには少なくとも一つのインデックスが入る

    引数:
    p (int): 現在の選手のインデックス。
    group (list): 現在の選手のグループ。
    n (int): 選手の総数。
    group_count (int): 希望するグループの総数。

    戻り値:
    list: 全ての可能なグループ分けのリスト。
    """
    # pがnに達し、group_countを満たしている場合groupを返す
    if idx == n:
        if len(group) == group_count:
            return [group]
    else:
        ret = []
        for j in range(len(group)):
            new_group = []
            for k in range(len(group)):
                if k == j:
                    # pをgroup jに追加
                    new_group.append(group[k] | {idx})
                else:
                    # pが加わらないgroupはそのまま
                    new_group.append(group[k].copy())
            # 探索をすすめる
            ret += find_all_groupings(idx + 1, new_group, n, group_count)
        # group数が満たなかった
        if len(group) < group_count:
            # 新しいグループを作り、pをそのグループに追加
            new_group = group + [{idx}]
            ret += find_all_groupings(idx + 1, new_group, n, group_count)
        return ret
    return []
