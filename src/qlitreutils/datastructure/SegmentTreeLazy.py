class LazySegmentTree:
    def __init__(self, init_val, mode):
        n = len(init_val)
        if mode not in ['rmiq', 'rmaq', 'rsq', 'rpq', 'rgcdq', 'rxorsq']:
            raise ValueError('modeは rmiq, rmaq, rsq, rgcdq のいずれかを指定してください')

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
        elif mode == 'rxorsq':
            self.seg_func = self.seg_func_range_xor_sum_query
            self.ide_ele = 0

        self.num = 1 << (n - 1).bit_length()
        self.data = [self.ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.seg_func(self.data[2 * i], self.data[2 * i + 1])

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

    @staticmethod
    def seg_func_range_xor_sum_query(x, y):
        """区間xor和"""
        return x ^ y

    def select(self, k):
        return self.data[k + self.num]

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while l < r:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v
            self.data[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.seg_func(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.seg_func(res, self.data[l])
                l += 1
            if r & 1:
                res = self.seg_func(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res
