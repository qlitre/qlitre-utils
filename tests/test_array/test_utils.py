from src.qlitreutils.array import utils


def test_get_connected_value_list():
    a_list = [(1, 2), (1, 3), (3, 6), (4, 5)]
    return_list = utils.get_connected_value_list(a_list, 1)
    assert return_list == [1, 2, 3, 6]
    return_list = utils.get_connected_value_list(a_list, 3)
    return_list.sort()
    assert return_list == [1, 2, 3, 6]
    a_list = [(1, 2), (1, 3), (3, 6), (4, 5), (6, 7, 8), (9,)]
    return_list = utils.get_connected_value_list(a_list, 3)
    return_list.sort()
    assert return_list == [1, 2, 3, 6, 7, 8]


def test_count_can_visit():
    data = {1: [2], 2: [3], 3: [4], 4: [1]}
    ans = 0
    for k in data.keys():
        ans += utils.count_can_visit(start=k, connected=data, include_start=True)
    assert ans == 16
    ans = 0
    for k in data.keys():
        ans += utils.count_can_visit(start=k, connected=data, include_start=False)
    assert ans == 12


def test_get_can_visit():
    data = {1: [2], 2: [1], 3: [4], 4: [1, 2]}
    ret = utils.get_can_visit(start=1, connected=data, include_start=True)
    ret.sort()
    assert ret == [1, 2]
    ret = utils.get_can_visit(start=2, connected=data, include_start=False)
    ret.sort()
    assert ret == [1]
    ret = utils.get_can_visit(start=3, connected=data, include_start=True)
    ret.sort()
    assert ret == [1, 2, 3, 4]
    ret = utils.get_can_visit(start=3, connected=data, include_start=False)
    ret.sort()
    assert ret == [1, 2, 4]
    ret = utils.get_can_visit(start=4, connected=data, include_start=True)
    ret.sort()
    assert ret == [1, 2, 4]
    ret = utils.get_can_visit(start=4, connected=data, include_start=False)
    ret.sort()
    assert ret == [1, 2]


def test_move_zeros_deque():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert utils.move_zeros_deque(a_list) == [1, 2, 3, 4, 5, 0, 0]


def test_move_zeros_basic():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert utils.move_zeros_deque(a_list) == [1, 2, 3, 4, 5, 0, 0]
