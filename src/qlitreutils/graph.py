"""
グラフ問題のヘルパー
"""
from collections import deque
import heapq


def get_connected_value_list(a_list: list, start_value) -> list:
    """
    タプルのリストを受け取り、繋がっている要素をリストにして返す
    例えばある地点からスタートして、どこまでたどり着けるか調べる
    warning:割と速度に不安がある。技術試験などでは辞書かして、get_can_visitを使った方がよい
    :param a_list ex.[(1, 2), (1, 3), (3, 6), (4, 5)]
    :param start_value 最初に調べる値、例えばスタート地点
    """
    ret = [start_value]
    checked = set()
    checked.add(start_value)
    que = deque([start_value])
    while que:
        check_val = que.popleft()
        for item in a_list:
            if check_val not in item:
                continue
            for elm in item:
                if elm in checked:
                    continue
                else:
                    ret.append(elm)
                    que.append(elm)
                    checked.add(elm)
    return ret


def count_can_visit(start, connected: dict, include_start: bool = False) -> int:
    """
    ある地点を起点に訪れることのできる場所の数を返す
    :param start:開始する数値、connectedのキーを指定
    :param connected:{0:[1,3,4],1:[2,3,4]...}
    :param include_start:開始地点を数に含めるか
    """
    checked = set()
    checked.add(start)
    cnt = 1 if include_start else 0
    que = deque()
    que.append(start)
    while que:
        now_place = que.popleft()
        for to_place in connected[now_place]:
            if to_place in checked:
                continue
            cnt += 1
            que.append(to_place)
            checked.add(to_place)
    return cnt


def get_can_visit(start, connected: dict, include_start: bool = False) -> list:
    """
    ある地点を起点に訪れることのできる場所をリストにして返す
    :param start:開始する数値、connectedのキーを指定
    :param connected:{0:[1,3,4],1:[2,3,4]...}
    :param include_start:開始地点を数に含めるか
    """
    checked = set()
    checked.add(start)
    ret = [start] if include_start else []
    que = deque()
    que.append(start)
    while que:
        now_place = que.popleft()
        for to_place in connected[now_place]:
            if to_place in checked:
                continue
            ret.append(to_place)
            que.append(to_place)
            checked.add(to_place)
    return ret


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

        for adj, cost in graph.get(pos, []):
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
