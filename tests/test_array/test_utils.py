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


def test_rotate_90():
    data = [[1, 2, 3],
            [4, 5, 6]]

    assert utils.rotate_90(data, 1) == [[3, 6],
                                        [2, 5],
                                        [1, 4]]

    assert utils.rotate_90(data, 2) == [[4, 5, 6], [1, 2, 3]]

    assert utils.rotate_90(data, 3) == [[4, 1],
                                        [5, 2],
                                        [6, 3]]

    assert utils.rotate_90(data, 4) == data

    assert utils.rotate_90(data, 5) == [[3, 6],
                                        [2, 5],
                                        [1, 4]]

    assert utils.rotate_90(data, 101) == [[3, 6],
                                          [2, 5],
                                          [1, 4]]

    _data = data.copy()
    # 4回やって元通りになるか
    for i in range(4):
        _data = utils.rotate_90(_data, 1)
    assert _data == data
