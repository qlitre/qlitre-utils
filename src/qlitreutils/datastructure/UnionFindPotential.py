class UnionFindPotential:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self._diff = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            root = self.find(self.parent[x])
            self._diff[x] += self._diff[self.parent[x]]  # Accumulate the difference
            self.parent[x] = root
            return root

    def union(self, x, y, d):
        px, py = self.find(x), self.find(y)
        if px == py:
            return self._diff[x] - self._diff[y] == d
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self._diff[px] = d - self._diff[x] + self._diff[y]
        else:
            self.parent[py] = px
            self._diff[py] = -d - self._diff[y] + self._diff[x]
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self._diff[x] - self._diff[y]
