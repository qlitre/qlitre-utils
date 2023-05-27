from src.qlitreutils.two_dimension import (is_three_points_on_same_line, get_length_between_two_points,
                                           check_square_by_line, get_square_point, get_center_point, get_rotate_point,
                                           get_max_manhattan_distance, calc_triangle_area)
import math
from pytest import approx


def test_is_three_points_on_same_line():
    x1, y1 = 0, 0
    x2, y2 = 1, 1
    x3, y3 = 2, 2
    assert is_three_points_on_same_line(x1, y1, x2, y2, x3, y3)
    x1, y1 = 0, 0
    x2, y2 = 1, 1
    x3, y3 = 4, 5
    assert not is_three_points_on_same_line(x1, y1, x2, y2, x3, y3)
    x1, y1 = 0, 0
    x2, y2 = 1, 0
    x3, y3 = 3, 0
    assert is_three_points_on_same_line(x1, y1, x2, y2, x3, y3)


def test_get_length_between_two_points():
    p1 = (1, 1)
    p2 = (1, 2)
    length = get_length_between_two_points(p1, p2)
    assert length == 1
    p1 = (1, 1)
    p2 = (2, 1)
    length = get_length_between_two_points(p1, p2)
    assert length == 1
    p1 = (1, 1)
    p2 = (2, 2)
    length = get_length_between_two_points(p1, p2)
    assert length == pow(2, 0.5)


def test_check_square_by_line():
    p1 = (0, 0)
    p2 = (1, 1)
    p3 = (1, 0)
    p4 = (0, 1)
    assert check_square_by_line(p1, p2, p3, p4)
    p1 = (0, 0)
    p2 = (1, 2)
    p3 = (1, 0)
    p4 = (0, 1)
    assert not check_square_by_line(p1, p2, p3, p4)
    # 斜め
    p1 = (1, 0)
    p2 = (0, 2)
    p3 = (3, 1)
    p4 = (2, 3)
    assert check_square_by_line(p1, p2, p3, p4)


def test_get_square_point():
    p1 = (2, 3)
    p2 = (3, 1)
    p3, p4 = get_square_point(p1, p2)
    assert p3 == (1, 0)
    assert p4 == (0, 2)


def test_get_center_point():
    point_1 = (1, 2)
    point_2 = (3, 4)
    ret = get_center_point(point_1, point_2)
    assert ret == (2, 3)


def test_get_rotate_point():
    # テストケース1: 90度回転
    point = (1, 0)
    degree = 90
    expected = (0, 1)
    assert get_rotate_point(point, degree) == approx(expected)

    # テストケース2: 45度回転
    point = (1, 1)
    degree = 45
    expected = (0, math.sqrt(2))
    assert get_rotate_point(point, degree) == approx(expected)

    # テストケース3: 180度回転
    point = (2, 3)
    degree = 180
    expected = (-2, -3)
    assert get_rotate_point(point, degree) == approx(expected)

    # テストケース4: 0度回転 (変化なし)
    point = (4, 5)
    degree = 0
    expected = (4, 5)
    assert get_rotate_point(point, degree) == approx(expected)


def test_get_max_manhattan_distance():
    points = [
        [1, 1],
        [2, 4],
        [3, 2]
    ]
    dist = get_max_manhattan_distance(points)
    assert dist == 4


def test_calc_triangle_area():
    area = calc_triangle_area(0, 0, 2, 0, 1, 2)
    assert area == 2
