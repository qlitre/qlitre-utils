from src.qlitreutils.search import utils


def test_get_nearest_value_in_list():
    an_iterable = [20, 13, 5, 1]
    target = -1
    assert utils.get_nearest_value_in_list(an_iterable, target) == 1
    target = 8
    assert utils.get_nearest_value_in_list(an_iterable, target) == 5
    target = 25
    assert utils.get_nearest_value_in_list(an_iterable, target) == 20


def test_binary_search():
    a_list = [10, 12, 13, 14, 15, 18, 19, 20]
    assert utils.binary_search(a_list, 19)
    print(utils.binary_search(a_list,17))


def test_binary_search_w_bisect():
    a_list = [10, 12, 13, 14, 15, 18, 19, 20]
    assert utils.binary_search_w_bisect(a_list, 19)
    assert not utils.binary_search_w_bisect(a_list, 21)
