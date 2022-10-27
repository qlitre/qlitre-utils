from src.qlitreutils.helper import two_dimension


def test_is_three_points_on_same_line():
    x1, y1 = 0, 0
    x2, y2 = 1, 1
    x3, y3 = 2, 2
    assert two_dimension.is_three_points_on_same_line(x1, y1, x2, y2, x3, y3)
    x1, y1 = 0, 0
    x2, y2 = 1, 1
    x3, y3 = 4, 5
    assert not two_dimension.is_three_points_on_same_line(x1, y1, x2, y2, x3, y3)
    x1, y1 = 0, 0
    x2, y2 = 1, 0
    x3, y3 = 3, 0
    assert two_dimension.is_three_points_on_same_line(x1, y1, x2, y2, x3, y3)
