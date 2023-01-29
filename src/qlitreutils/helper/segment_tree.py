"""
セグメントツリークラス
"""
import typing


class SegTree:
    """
    参考:https://qiita.com/takayg1/items/c811bd07c21923d7ec69
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, mode: typing.Literal['rmiq', 'rmaq', 'rsq', 'rpq', 'rgcdq']):
        """
        init_val: 配列の初期値
        mode:
            'rmiq':区間最小
            'rmaq':区間最大
            'rsq':区間和
            'rpq':区間積
            'rgcdq':区間最大公約数
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.seg_func = None
        if mode == 'rmiq':
            self.seg_func = self.seg_func_range_min_query
            self.ide_ele = 10 ** 18
        elif mode == 'rmaq':
            self.seg_func = self.seg_func_range_max_query
            self.ide_ele = -10 ** 18
        elif mode == 'rsq':
            self.seg_func = self.seg_func_range_sum_query
            self.ide_ele = 0
        elif mode == 'rpq':
            self.seg_func = self.seg_func_range_product
            self.ide_ele = 1
        elif mode == 'rgcdq':
            self.seg_func = self.seg_func_range_gcd
            self.ide_ele = 0

        self.num = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.seg_func(self.tree[2 * i], self.tree[2 * i + 1])

    @staticmethod
    def seg_func_range_sum_query(x, y):
        """区間和"""
        return x + y

    @staticmethod
    def seg_func_range_min_query(x, y):
        """区間最小"""
        return min(x, y)

    @staticmethod
    def seg_func_range_max_query(x, y):
        """区間最大"""
        return max(x, y)

    @staticmethod
    def seg_func_range_product(x, y):
        """区間積"""
        return x * y

    @staticmethod
    def seg_func_range_gcd(x, y):
        """区間最大公約数"""
        import math
        return math.gcd(x, y)

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.seg_func(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.seg_func(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.seg_func(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
