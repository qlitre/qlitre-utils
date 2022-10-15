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
