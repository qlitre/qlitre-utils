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


def meguru_bisect(ng, ok):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """

    def is_ok(arg):
        pass

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
