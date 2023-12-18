from src.qlitreutils.graph import (get_tree_simple_path,
                                   get_double_sweep, check_bipartite, bipartite_graph_separate_two_color, dijkstra,
                                   get_dijkstra_root, topological_sort, euler_tour, warshall_floyd)
from collections import defaultdict


def test_get_tree_simple_path():
    data = {3: [1], 1: [3, 2, 4], 2: [5, 1, 6], 5: [2], 4: [1], 6: [2]}
    ret = get_tree_simple_path(6, data, 1, 2)
    assert ret == [1, 2]

    data = {1: [2, 3], 2: [1], 3: [1, 4, 5], 4: [3], 5: [3]}
    ret = get_tree_simple_path(5, data, 2, 5)
    assert ret == [2, 1, 3, 5]


def test_get_double_sweep():
    data = {1: [2], 2: [1, 3], 3: [2]}
    assert get_double_sweep(data, 3, 1) == 2
    data = {1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3], 5: [3]}
    assert get_double_sweep(data, 5, 1) == 3


def test_check_bipartite():
    from collections import defaultdict

    colors = defaultdict(int)
    data = defaultdict(list)
    """
    3 1
    2 0
    4 1
    2 1
    """
    data[3].append(1)
    data[1].append(3)
    data[2].append(0)
    data[0].append(2)
    data[4].append(1)
    data[1].append(4)
    data[2].append(1)
    data[1].append(2)
    flg, colors, group = check_bipartite(data, colors, 0)
    for k, v in group.items():
        for vertex in v:
            assert colors[vertex] == k

    assert flg

    # flg=Falseを検証
    data = defaultdict(list)
    colors = defaultdict(int)
    """
    2 0
    2 1
    0 1
    """
    data[2].append(0)
    data[0].append(2)
    data[2].append(1)
    data[1].append(2)
    data[0].append(1)
    data[1].append(0)
    flg, colors, group = check_bipartite(data, colors, 0)
    for k, v in group.items():
        for vertex in v:
            assert colors[vertex] == k
    assert not flg


def test_bipartite_graph_separate_two_color():
    data = {1: [3], 3: [1, 5, 6], 6: [3], 5: [3, 2], 2: [5, 4], 4: [2]}
    group = bipartite_graph_separate_two_color(data, 1)
    g1 = sorted(group[0])
    g2 = sorted(group[1])
    assert g1 == [1, 4, 5, 6]
    assert g2 == [2, 3]


def test_dijkstra():
    n = 6
    data = {1: [(2, 15), (4, 20)], 2: [(1, 15), (3, 65), (5, 4)], 4: [(1, 20), (5, 30)], 3: [(2, 65), (6, 50)],
            5: [(2, 4), (4, 30), (6, 8)], 6: [(3, 50), (5, 8)]}
    dis = dijkstra(n=n, graph=data, start_vertex=1)
    assert dis == [10 ** 18, 0, 15, 77, 20, 19, 27]


def test_get_dijkstra_root():
    n = 6
    data = {1: [(2, 15), (4, 20)], 2: [(1, 15), (3, 65), (5, 4)], 4: [(1, 20), (5, 30)], 3: [(2, 65), (6, 50)],
            5: [(2, 4), (4, 30), (6, 8)], 6: [(3, 50), (5, 8)]}
    root = get_dijkstra_root(n=n, graph=data, start_vertex=1, end_vertex=n)
    assert root == [1, 2, 5, 6]


def test_topological_sort():
    _graph = defaultdict(list)

    n = 4
    into_num = [0] * n
    edges = [
        (2, 1),
        (3, 4),
        (2, 4),
    ]
    for a, b in edges:
        a -= 1
        b -= 1
        _graph[a].append(b)
        into_num[b] += 1
    res = topological_sort(n, _graph, into_num)
    assert res == [2, 1, 3, 4]

    n = 4
    into_num = [0] * n
    edges = [
        (1, 2),
        (1, 2),
        (2, 1),
    ]
    for a, b in edges:
        a -= 1
        b -= 1
        _graph[a].append(b)
        into_num[b] += 1
    res = topological_sort(n, _graph, into_num)
    assert res == []


def test_euler_tour():
    # グラフの構築
    _graph = {0: [3, 1], 3: [0], 1: [0, 4, 2], 4: [1], 2: [1]}
    n = len(_graph)

    # euler_tour関数の実行
    tour, in_time, out_time = euler_tour(n, _graph, 0)
    # 結果の検証
    assert tour == [0, 1, 2, 1, 4, 1, 0, 3, 0]
    assert in_time == [0, 1, 2, 7, 4]
    assert out_time == [9, 6, 3, 8, 5]

    # グラフの構築
    _graph = {0: [3, 1], 3: [0, 5], 1: [0, 4, 2], 4: [1], 2: [1], 5: [3]}
    n = len(_graph)

    # euler_tour関数の実行
    tour, in_time, out_time = euler_tour(n, _graph, 0)
    # 結果の検証
    assert tour == [0, 1, 2, 1, 4, 1, 0, 3, 5, 3, 0]
    assert in_time == [0, 1, 2, 7, 4, 8]
    assert out_time == [11, 6, 3, 10, 5, 9]


def test_warshall_floyd():
    inf = float('inf')
    cost = [
        [0, 5, 7, inf, inf],
        [5, 0, 2, 4, inf],
        [7, 2, 0, 1, inf],
        [inf, 4, 1, 0, 3],
        [inf, inf, inf, 3, 0]
    ]
    expected = [
        [0, 5, 7, 8, 11],
        [5, 0, 2, 3, 6],
        [7, 2, 0, 1, 4],
        [8, 3, 1, 0, 3],
        [11, 6, 4, 3, 0]
    ]
    result = warshall_floyd(cost)
    assert result == expected

    cost = [
        [0, 1, inf, inf],
        [1, 0, 1, inf],
        [inf, 1, 0, 1],
        [inf, inf, 1, 0]
    ]
    expected = [
        [0, 1, 2, 3],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [3, 2, 1, 0]
    ]
    result = warshall_floyd(cost)
    assert result == expected
