from src.qlitreutils import array
from typing import List


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


def test_generate_zigzag_indices():
    def check(_arr: List[List[int]], _expected: List[List[int]]):
        result = array.generate_zigzag_indices(_arr)
        assert result == _expected, f"Expected {expected}, but got {result}"

        # Test case 1: 2x2 array
        arr = [
            [1, 2],
            [3, 4]
        ]
        expected = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0]
        ]
        check(arr, expected)

        # Test case 2: 3x3 array
        arr = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 2],
            [1, 1],
            [1, 0],
            [2, 0],
            [2, 1],
            [2, 2]
        ]
        check(arr, expected)

        # Test case 3: 2x3 array
        arr = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        expected = [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 2],
            [1, 1],
            [1, 0]
        ]
        check(arr, expected)

        # Test case 4: 3x2 array
        arr = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        expected = [
            [0, 0],
            [0, 1],
            [1, 1],
            [2, 1],
            [2, 0],
            [1, 0]
        ]
        check(arr, expected)
