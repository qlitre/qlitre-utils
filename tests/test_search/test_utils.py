from src.qlitreutils.search import utils


def test_get_nearest_value_in_list():
    an_iterable = [20, 13, 5, 1]
    target = -1
    assert utils.get_nearest_value_in_list(an_iterable, target) == 1
    target = 8
    assert utils.get_nearest_value_in_list(an_iterable, target) == 5
    target = 25
    assert utils.get_nearest_value_in_list(an_iterable, target) == 20
