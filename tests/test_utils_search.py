from src.qlitreutils import utils_search


def test_get_nearest_value_in_list():
    an_iterable = [20, 13, 5, 1]
    target = -1
    assert utils_search.get_nearest_value_in_list(an_iterable, target) == 1
    target = 8
    assert utils_search.get_nearest_value_in_list(an_iterable, target) == 5
    target = 25
    assert utils_search.get_nearest_value_in_list(an_iterable, target) == 20


def test_binary_search():
    a_list = [10, 12, 13, 14, 15, 18, 19, 20]
    assert utils_search.binary_search(a_list, 19)
    print(utils_search.binary_search(a_list, 17))


def test_binary_search_w_bisect():
    a_list = [10, 12, 13, 14, 15, 18, 19, 20]
    assert utils_search.binary_search_w_bisect(a_list, 19)
    assert not utils_search.binary_search_w_bisect(a_list, 21)
