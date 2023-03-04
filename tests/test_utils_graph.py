from src.qlitreutils import utils_graph


def test_get_connected_value_list():
    a_list = [(1, 2), (1, 3), (3, 6), (4, 5)]
    return_list = utils_graph.get_connected_value_list(a_list, 1)
    assert return_list == [1, 2, 3, 6]
    return_list = utils_graph.get_connected_value_list(a_list, 3)
    return_list.sort()
    assert return_list == [1, 2, 3, 6]
    a_list = [(1, 2), (1, 3), (3, 6), (4, 5), (6, 7, 8), (9,)]
    return_list = utils_graph.get_connected_value_list(a_list, 3)
    return_list.sort()
    assert return_list == [1, 2, 3, 6, 7, 8]


def test_count_can_visit():
    data = {1: [2], 2: [3], 3: [4], 4: [1]}
    ans = 0
    for k in data.keys():
        ans += utils_graph.count_can_visit(start=k, connected=data, include_start=True)
    assert ans == 16
    ans = 0
    for k in data.keys():
        ans += utils_graph.count_can_visit(start=k, connected=data, include_start=False)
    assert ans == 12


def test_get_can_visit():
    data = {1: [2], 2: [1], 3: [4], 4: [1, 2]}
    ret = utils_graph.get_can_visit(start=1, connected=data, include_start=True)
    ret.sort()
    assert ret == [1, 2]
    ret = utils_graph.get_can_visit(start=2, connected=data, include_start=False)
    ret.sort()
    assert ret == [1]
    ret = utils_graph.get_can_visit(start=3, connected=data, include_start=True)
    ret.sort()
    assert ret == [1, 2, 3, 4]
    ret = utils_graph.get_can_visit(start=3, connected=data, include_start=False)
    ret.sort()
    assert ret == [1, 2, 4]
    ret = utils_graph.get_can_visit(start=4, connected=data, include_start=True)
    ret.sort()
    assert ret == [1, 2, 4]
    ret = utils_graph.get_can_visit(start=4, connected=data, include_start=False)
    ret.sort()
    assert ret == [1, 2]


def test_get_tree_simple_path():
    graph = {3: [1], 1: [3, 2, 4], 2: [5, 1, 6], 5: [2], 4: [1], 6: [2]}
    ret = utils_graph.get_tree_simple_path(6, graph, 1, 2)
    assert ret == [1, 2]

    graph = {1: [2, 3], 2: [1], 3: [1, 4, 5], 4: [3], 5: [3]}
    ret = utils_graph.get_tree_simple_path(5, graph, 2, 5)
    assert ret == [2, 1, 3, 5]


def test_get_double_sweep():
    data = {1: [2], 2: [1, 3], 3: [2]}
    assert utils_graph.get_double_sweep(data, 3, 1) == 2
    data = {1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3], 5: [3]}
    assert utils_graph.get_double_sweep(data, 5, 1) == 3


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
    flg, colors, group = utils_graph.check_bipartite(data, colors, 0)
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
    flg, colors, group = utils_graph.check_bipartite(data, colors, 0)
    for k, v in group.items():
        for vertex in v:
            assert colors[vertex] == k
    assert not flg


def test_bipartite_graph_separate_two_color():
    data = {1: [3], 3: [1, 5, 6], 6: [3], 5: [3, 2], 2: [5, 4], 4: [2]}
    group = utils_graph.bipartite_graph_separate_two_color(data, 1)
    g1 = sorted(group[0])
    g2 = sorted(group[1])
    assert g1 == [1, 4, 5, 6]
    assert g2 == [2, 3]


def test_dijkstra():
    n = 6
    graph = {1: [(2, 15), (4, 20)], 2: [(1, 15), (3, 65), (5, 4)], 4: [(1, 20), (5, 30)], 3: [(2, 65), (6, 50)],
             5: [(2, 4), (4, 30), (6, 8)], 6: [(3, 50), (5, 8)]}
    dis = utils_graph.dijkstra(n=n, graph=graph, start_vertex=1)
    assert dis == [10 ** 18, 0, 15, 77, 20, 19, 27]


def test_get_dijkstra_root():
    n = 6
    graph = {1: [(2, 15), (4, 20)], 2: [(1, 15), (3, 65), (5, 4)], 4: [(1, 20), (5, 30)], 3: [(2, 65), (6, 50)],
             5: [(2, 4), (4, 30), (6, 8)], 6: [(3, 50), (5, 8)]}
    root = utils_graph.get_dijkstra_root(n=n, graph=graph, start_vertex=1, end_vertex=n)
    assert root == [1, 2, 5, 6]