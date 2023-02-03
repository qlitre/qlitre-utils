class FordFulkerson:
    """
    FordFulkerson法
    最大フロー問題で使用する
    """

    def __init__(self, n):
        self.used = None
        self.N = n
        self.G = [[] for i in range(n)]
        self.inf = 10 ** 18

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        f = self.inf
        while f:
            self.used = [0] * self.N
            f = self.dfs(s, t, self.inf)
            flow += f
        return flow
