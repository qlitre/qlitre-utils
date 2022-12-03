"""
セグメントツリークラス
"""


class SegTree:
    def __init__(self, x_list, init, seg_func):
        self.init = init
        self.seg_func = seg_func
        self.Height = len(x_list).bit_length() + 1
        self.Tree = [init] * (2 ** self.Height)
        self.num = 2 ** (self.Height - 1)
        for i in range(len(x_list)):
            self.Tree[2 ** (self.Height - 1) + i] = x_list[i]
        for i in range(2 ** (self.Height - 1) - 1, 0, -1):
            self.Tree[i] = seg_func(self.Tree[2 * i], self.Tree[2 * i + 1])

    def select(self, k):
        return self.Tree[k + self.num]

    def update(self, k, x):
        i = k + self.num
        self.Tree[i] = x
        while i > 1:
            if i % 2 == 0:
                self.Tree[i // 2] = self.seg_func(self.Tree[i], self.Tree[i + 1])
            else:
                self.Tree[i // 2] = self.seg_func(self.Tree[i - 1], self.Tree[i])
            i //= 2

    def query(self, left, right):
        result = self.init
        left += self.num
        right += self.num + 1

        while left < right:
            if left % 2 == 1:
                result = self.seg_func(result, self.Tree[left])
                left += 1
            if right % 2 == 1:
                result = self.seg_func(result, self.Tree[right - 1])
            left //= 2
            right //= 2
        return result
