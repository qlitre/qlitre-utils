from src.qlitreutils import array


def test_move_zeros_deque():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert array.move_zeros_deque(a_list) == [1, 2, 3, 4, 5, 0, 0]


def test_move_zeros_basic():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert array.move_zeros_deque(a_list) == [1, 2, 3, 4, 5, 0, 0]


def test_generate_round_trip_value():
    a_list = [1, 2, 3, 4]
    ret = array.generate_round_trip_value(a_list, 9)
    assert list(ret) == [1, 2, 3, 4, 3, 2, 1, 2, 3]


def test_get_difference_sequence():
    a_list = [1, 2, 3, 4]
    ret = array.get_difference_sequence(a_list)
    assert ret == [1, 1, 1]
    a_list = [1, -3, 2, 5]
    ret = array.get_difference_sequence(a_list)
    assert ret == [-4, 5, 3]


def test_count_inversion():
    a_list = [1, 3, 4, 2]
    count = array.count_inversion(a_list)
    assert count == 2
    a_list = [1, 2, 3, 4]
    count = array.count_inversion(a_list)
    assert count == 0
    a_list = [4, 3, 2, 1]
    count = array.count_inversion(a_list)
    assert count == 6


def test_rotate_90():
    data = [[1, 2, 3],
            [4, 5, 6]]
    ret = array.rotate_90(data)
    assert ret == [[3, 6],
                   [2, 5],
                   [1, 4]]

    ret = array.rotate_90(ret)
    assert ret == [[6, 5, 4],
                   [3, 2, 1]]

    ret = array.rotate_90(ret)
    assert ret == [[4, 1],
                   [5, 2],
                   [6, 3]]

    ret = array.rotate_90(ret)
    assert ret == data
