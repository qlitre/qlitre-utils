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


def gen_decreasing_seq(length: int, limit: int) -> list:
    ret = []
    que = deque()
    for i in range(limit, 0, -1):
        que.append(([i], 1))

    while que:
        al, depth = que.popleft()
        if depth == length:
            ret.append(al)
        else:
            last = al[-1]
            # 0を含める場合はrange(last - 1, -1, -1)とする
            for i in range(last - 1, 0, -1):
                que.append((al + [i], depth + 1))

    return ret


def find_all_groupings(p: int, groups: list, n: int, group_count: int) -> list:
    """
    n人をgroup_count数のグループに分けるような組み合わせを全列挙して返す
    :param p:startのインデックス。大体０で始まる
    :param groups: グループ分け組み合わせ。最初は空の配列を渡す
    :param n:総人間数
    :param group_count:
    :return:[[groups],[groups]...]
    """
    if p == n:
        if len(groups) == group_count:
            return [groups]
        else:
            return []
    else:
        res = []
        for j, group in enumerate(groups):
            new_groups = groups.copy()
            new_group = group.copy()
            new_group.append(p)
            new_groups[j] = new_group
            res += find_all_groupings(p + 1, new_groups, n, group_count)
        # group_count未満だったらgroupを増やす
        if len(groups) < group_count:
            new_groups = groups.copy()
            new_groups.append([p])
            res += find_all_groupings(p + 1, new_groups, n, group_count)
        return res


def generate_pairs(lst):
    """
    与えられたリストの要素（人間）を2人1組に分ける全ての組み合わせを生成する関数。
    これは再帰的な方法でペアを生成します。

    Parameters
    ----------
    lst : list
        人間のリスト。各人間は一意であると仮定します。

    Returns
    -------
    all_pairs : list of list of tuple
        人間を2人1組に分ける全ての組み合わせ。各組み合わせは、人間のペア（タプル）のリストとして表されます。

    Example
    --------
    >>> generate_pairs(['A', 'B', 'C', 'D'])
    [[('A', 'B'), ('C', 'D')], [('A', 'C'), ('B', 'D')], [('A', 'D'), ('B', 'C')]]
    """
    if len(lst) < 2:
        return []
    if len(lst) == 2:
        return [[(lst[0], lst[1])]]

    # すべてのペアを格納するリスト
    all_pairs = []

    # 先頭の要素（1つ目の人）を取り出す
    first = lst[0]

    # 先頭の要素とペアになる要素（2つ目以降の人）を繰り返し取り出す
    for i in range(1, len(lst)):
        # 先頭の要素とi番目の要素のペアを作る
        pair = (first, lst[i])

        # 残りの要素から再帰的にペアを生成する
        rest = lst[1:i] + lst[i + 1:]
        for p in generate_pairs(rest):
            all_pairs.append([pair] + p)

    return all_pairs
