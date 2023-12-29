from src.qlitreutils.array import (
    move_zeros_deque,
    move_zeros_basic,
    generate_round_trip_value,
    count_inversion,
    rotate_90,
    generate_zigzag_indices,
    get_difference_sequence,
    get_lis
)
from typing import List


def test_move_zeros_deque():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert move_zeros_deque(a_list) == [1, 2, 3, 4, 5, 0, 0]


def test_move_zeros_basic():
    a_list = [1, 2, 0, 3, 0, 4, 5]
    assert move_zeros_basic(a_list) == [1, 2, 3, 4, 5, 0, 0]


def test_generate_round_trip_value():
    a_list = [1, 2, 3, 4]
    ret = generate_round_trip_value(a_list, 9)
    assert list(ret) == [1, 2, 3, 4, 3, 2, 1, 2, 3]


def test_get_difference_sequence():
    a_list = [1, 2, 3, 4]
    ret = get_difference_sequence(a_list)
    assert ret == [1, 1, 1]
    a_list = [1, -3, 2, 5]
    ret = get_difference_sequence(a_list)
    assert ret == [-4, 5, 3]


def test_count_inversion():
    a_list = [1, 3, 4, 2]
    count = count_inversion(a_list)
    assert count == 2
    a_list = [1, 2, 3, 4]
    count = count_inversion(a_list)
    assert count == 0
    a_list = [4, 3, 2, 1]
    count = count_inversion(a_list)
    assert count == 6


def test_rotate_90():
    data = [[1, 2, 3],
            [4, 5, 6]]
    ret = rotate_90(data)
    assert ret == [[3, 6],
                   [2, 5],
                   [1, 4]]

    ret = rotate_90(ret)
    assert ret == [[6, 5, 4],
                   [3, 2, 1]]

    ret = rotate_90(ret)
    assert ret == [[4, 1],
                   [5, 2],
                   [6, 3]]

    ret = rotate_90(ret)
    assert ret == data


def test_generate_zigzag_indices():
    def check(_arr: List[List[int]], _expected: List[List[int]]):
        result = generate_zigzag_indices(_arr)
        assert result == _expected

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
        [1, 0],
        [2, 0],
        [2, 1],
    ]
    check(arr, expected)


def test_get_lis():
    al = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    expect = [1, 2, 1, 3, 2, 4, 4, 5, 6]
    assert get_lis(al) == expect
    al = [3, 10, 2, 1, 20]
    expect = [1, 2, 1, 1, 3]
    assert get_lis(al) == expect
    al = [3, 2]
    expect = [1, 1]
    assert get_lis(al) == expect
    assert get_lis([]) == []
