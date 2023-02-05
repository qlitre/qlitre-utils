from src.qlitreutils.array import utils


def test_move_zeros_deque():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert utils.move_zeros_deque(a_list) == [1, 2, 3, 4, 5, 0, 0]


def test_move_zeros_basic():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert utils.move_zeros_deque(a_list) == [1, 2, 3, 4, 5, 0, 0]


def test_generate_round_trip_value():
    a_list = [1, 2, 3, 4]
    ret = utils.generate_round_trip_value(a_list, 9)
    assert list(ret) == [1, 2, 3, 4, 3, 2, 1, 2, 3]


def test_get_difference_sequence():
    a_list = [1, 2, 3, 4]
    ret = utils.get_difference_sequence(a_list)
    assert ret == [1, 1, 1]
    a_list = [1, -3, 2, 5]
    ret = utils.get_difference_sequence(a_list)
    assert ret == [-4, 5, 3]


def test_count_inversion():
    a_list = [1, 3, 4, 2]
    count = utils.count_inversion(a_list)
    assert count == 2
    a_list = [1, 2, 3, 4]
    count = utils.count_inversion(a_list)
    assert count == 0
    a_list = [4, 3, 2, 1]
    count = utils.count_inversion(a_list)
    assert count == 6
