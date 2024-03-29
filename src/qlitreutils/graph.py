"""
グラフ問題のヘルパー
"""
from collections import deque, defaultdict
import heapq


def get_tree_simple_path(n: int, graph: dict, start_vertex: int, end_vertex):
    """頂点から頂点への単純パスを返す"""
    vis = set()
    que = deque()
    vis.add(start_vertex)
    que.append(start_vertex)
    root = [-1] * (n + 1)

    # 幅優先探索してルートを記録
    while que:
        now = que.popleft()
        if now == end_vertex:
            break
        conn = graph[now]
        for adj in conn:
            if adj in vis:
                continue
            else:
                vis.add(adj)
                que.append(adj)
                root[adj] = now

    idx = end_vertex
    ret = [end_vertex]
    while True:
        bef = root[idx]
        if bef == start_vertex:
            ret.append(start_vertex)
            break
        # たどり着けなかった
        elif bef == -1:
            return -1
        else:
            ret.append(bef)
            idx = bef

    ret.reverse()
    return ret


def get_double_sweep(data: dict, n_vertex: int, start_vertex: int) -> int:
    """
    :param data: 木構造データ
    :param n_vertex: 頂点数
    :param start_vertex: 開始する頂点
    :return: 木の直径を返す
    """

    def max_dist_and_node_using_bfs(start):
        """幅優先探索をして最大距離"""
        checked = set()
        checked.add(start)
        que = deque([start])
        move_count = [0] * (n_vertex + 1)
        max_dist_node = (-10 ** 15, 0)
        while que:
            current_node = que.popleft()
            next_node_list = data[current_node]
            for to_node in next_node_list:
                if to_node in checked:
                    continue
                else:
                    checked.add(to_node)
                    que.append(to_node)
                    count = move_count[current_node] + 1
                    move_count[to_node] = count
                    a_count = max_dist_node[0]
                    if count >= a_count:
                        max_dist_node = (count, to_node)

        return max_dist_node

    a_max_item = max_dist_and_node_using_bfs(start_vertex)
    max_node = a_max_item[1]
    ret = max_dist_and_node_using_bfs(max_node)
    return ret[0]


def check_bipartite(graph: dict, colors: dict, s_vertex: int):
    """
    :param graph:リストの辞書
    :param colors:頂点毎に-1か1の辞書で管理
    :param s_vertex:探索を始める頂点
    :return:二部グラフかどうかの判定、更新したcolors、group
    """
    stack = deque([])
    group = {1: [], -1: []}
    stack.append([s_vertex, 1])
    while stack:
        now_vertex, color = stack.pop()
        if colors[now_vertex] == 0:
            group[color].append(now_vertex)
            colors[now_vertex] = color
            for to in graph[now_vertex]:
                if colors[to] == color:
                    return False, colors, group
                if colors[to] == 0:
                    stack.append([to, -1 * color])
    return True, colors, group


def bipartite_graph_separate_two_color(graph: dict, start_vertex: int) -> list:
    """２部グラフを隣接しない頂点に分けて返す"""
    group = [[], []]
    # 今いる頂点・一つ前の頂点・組(0 or 1)
    que = [(start_vertex, start_vertex - 1, 0)]
    while que:
        vertex, past, color = que.pop()
        group[color].append(vertex)
        # 今いる頂点に隣接しているノードを見る
        for i in graph[vertex]:
            if i == past:
                continue

            que.append((i, vertex, color ^ 1))

    return group


def dijkstra(n: int, graph: dict, start_vertex: int) -> list:
    """
    ダイクストラしてある地点からの最短距離のリストを返す
    :param n: 頂点数
    :param graph: 辞書 {頂点1:[(頂点2,cost),(頂点3,cost)...]}という形式
    :param start_vertex:スタートする頂点
    """
    inf = 10 ** 18
    cur = [inf] * (n + 1)
    cur[start_vertex] = 0
    vis = set()
    que = [(0, start_vertex)]
    heapq.heapify(que)
    while len(que) >= 1:
        pos = heapq.heappop(que)[1]
        if pos in vis:
            continue
        vis.add(pos)

        for adj, cost in graph[pos]:
            distance = cur[pos] + cost
            if distance < cur[adj]:
                cur[adj] = distance
                heapq.heappush(que, (distance, adj))

    return cur


def get_dijkstra_root(n: int, graph: dict, start_vertex: int, end_vertex: int):
    """
    ダイクストラしてある地点からの最短距離の経路を返す
    :param n: 頂点数
    :param graph: 辞書 {頂点1:[(頂点2,cost),(頂点3,cost)...]}という形式
    :param start_vertex:スタートする頂点
    :param end_vertex:終了する頂点
    """
    inf = 10 ** 18
    cur = [inf] * (n + 1)
    cur[start_vertex] = 0
    vis = set()
    que = [(0, start_vertex)]
    heapq.heapify(que)
    roots = [-1] * (n + 1)
    while len(que) >= 1:
        pos = heapq.heappop(que)[1]
        if pos in vis:
            continue
        vis.add(pos)

        for adj, cost in graph[pos]:
            distance = cur[pos] + cost
            if distance < cur[adj]:
                cur[adj] = distance
                heapq.heappush(que, (distance, adj))
                roots[adj] = pos

    # 復元処理
    now = end_vertex
    ret = [now]
    while True:
        nxt = roots[now]
        ret.append(nxt)
        if nxt == start_vertex:
            break
        else:
            now = nxt
    ret.reverse()
    return ret


def topological_sort(n: int, graph: dict, into_num: list) -> list:
    """
    トポロジカルソートした配列を返す
    トポロジカルソート出来なかった場合は空の配列を返す。
    ※注意 now +1 して返す
    :param n:頂点数
    :param graph: {a:[b,c,d],e:[f]...}
    :param into_num: 次数の配列
    """
    que = []
    for i in range(n):
        if into_num[i] == 0:
            que.append(i)
    ret = []
    while que:
        now = heapq.heappop(que)
        ret.append(now + 1)
        for adj in graph[now]:
            into_num[adj] -= 1
            if into_num[adj] == 0:
                heapq.heappush(que, adj)

    if len(ret) == n:
        return ret
    else:
        return []


def euler_tour(n: int, graph: dict, root: int):
    """
    :param n: 頂点数
    :param graph: 2D matrix of N vertices given by the edges
    :param root: 開始頂点のインデックス

    :return tour: 訪問した頂点の順序
    :return in_time: 各頂点の最初の訪問時刻
    :return out_time: 各頂点の最後の訪問時刻

    ex)
    tour, in_time, out_time = euler_tour(n, graph, 0)
    """

    parent = [-1] * n
    # postorder, preorder
    stack = [~root, root]
    curr_time = -1
    tour = []
    in_time = [-1] * n
    out_time = [-1] * n
    while stack:
        curr_node = stack.pop()
        curr_time += 1
        # preorder
        if curr_node >= 0:
            tour.append(curr_node)
            if in_time[curr_node] == -1:
                in_time[curr_node] = curr_time

            for next_node in graph[curr_node]:
                if next_node != parent[curr_node]:
                    parent[next_node] = curr_node
                    stack.append(~next_node)
                    stack.append(next_node)
        # postorder
        elif curr_node < 0:
            out_time[~curr_node] = curr_time
            if parent[~curr_node] != -1:
                tour.append(parent[~curr_node])

    return tour, in_time, out_time


def count_subtree(graph: dict, start_vertex: int) -> dict:
    """
    隣接リストで表されるグラフと開始頂点が与えられたとき、この関数は各頂点のサブツリーに含まれる頂点の数を計算します。
    この関数はスタックを使用した深さ優先探索（DFS）アルゴリズムを用いてグラフを走査し、
    各頂点を根とするサブツリーに含まれる頂点の数をカウントして辞書に格納します。
    パラメータ:
    graph (dict): グラフを表す辞書。キーは頂点の識別子（整数）で、値は隣接する頂点のリストです。
    start_vertex (int): DFS走査を開始する頂点。
    戻り値:
    dict: キーがグラフの頂点、値がその頂点を根とするサブツリーに含まれる頂点の数を表す辞書。
         各頂点は自身のサブツリーのカウントに含まれます。

   例:
   グラフが {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]} で、start_vertex = 1 の場合、
   関数は {0: 4, 1: 4, 2: 2, 3: 1, 4: 1} を返します。
   """
    stack = [(start_vertex - 1, start_vertex, True)]
    ret = defaultdict(lambda: 1)
    vis = set()
    vis.add(start_vertex)
    while stack:
        pre, now, f = stack.pop()
        if f:
            for adj in graph[now]:
                if pre == adj or adj in vis:
                    continue
                vis.add(adj)
                stack.append((now, adj, False))
                stack.append((now, adj, True))
        else:
            ret[pre] += ret[now]
    return ret


def warshall_floyd(cost):
    """
    隣接行列で表現されたグラフにワーシャル・フロイド法を適用し、
    すべての頂点ペア間の最短距離を計算して返す。
    :param cost :List[List[int]] グラフの隣接行列。頂点 i から頂点 j までの距離またはコストを表す。
                cost[i][j] が inf の場合、頂点 i と頂点 j の間に直接的な接続がないことを示す。
    :return:List[List[int]]: すべての頂点ペア間の最短距離を計算した後の隣接行列。
    """

    num_vertices = len(cost)

    for mid_k in range(num_vertices):
        for start_i in range(num_vertices):
            for end_j in range(num_vertices):
                cost[start_i][end_j] = min(cost[start_i][end_j], cost[start_i][mid_k] + cost[mid_k][end_j])
    return cost
