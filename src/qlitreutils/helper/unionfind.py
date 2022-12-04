"""
ユニオンファインド問題のヘルパー
"""

from collections import defaultdict


class UnionFindSimple:
    """要素に整数を使用するUnionFind"""

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


class UnionFindMultiple:
    def __init__(self):
        """
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        """
        self.parents = dict()  # {子要素:親ID,}
        self.members_set = defaultdict(lambda: set())  # keyが根でvalueが根に属する要素要素(tupleや文字列可)
        self.roots_set = set()  # 根の集合(tupleや文字列可)
        self.key_ID = dict()  # 各要素にIDを割り振る
        self.ID_key = dict()  # IDから要素名を復元する
        self.cnt = 0  # IDのカウンター

    def dict_find(self, x):  # 要素名とIDをやり取りするところ
        if x in self.key_ID:
            return self.key_ID[x]
        else:
            self.cnt += 1
            self.key_ID[x] = self.cnt
            self.parents[x] = self.cnt
            self.ID_key[self.cnt] = x
            self.members_set[x].add(x)
            self.roots_set.add(x)
            return self.key_ID[x]

    def find(self, x):
        id_x = self.dict_find(x)
        if self.parents[x] == id_x:
            return x
        else:
            self.parents[x] = self.key_ID[self.find(self.ID_key[self.parents[x]])]
            return self.ID_key[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in self.members_set[y]:
            self.members_set[x].add(i)
        self.members_set[y] = set()
        self.roots_set.remove(y)
        self.parents[y] = self.key_ID[x]

    def size(self, x):  # xが含まれる集合の要素数
        return len(self.members_set[self.find(x)])

    def same(self, x, y):  # 同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):  # xを含む集合の要素
        return self.members_set[self.find(x)]

    def roots(self):  # 根の要素
        return self.roots_set

    def group_count(self):  # 根の数
        return len(self.roots_set)

    def all_group_members(self):  # 根とその要素
        return {r: self.members_set[r] for r in self.roots_set}
