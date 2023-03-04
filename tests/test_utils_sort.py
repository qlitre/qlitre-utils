from src.qlitreutils import utils_sort


def test_bubble_sort():
    my_list = [6, 5, 8, 2]
    my_list = utils_sort.bubble_sort(my_list)
    assert my_list == [2, 5, 6, 8]


def test_insertion_sort():
    my_list = [6, 5, 8, 2]
    my_list = utils_sort.insertion_sort(my_list)
    assert my_list == [2, 5, 6, 8]


def test_merge_sort():
    my_list = [6, 5, 8, 2]
    my_list = utils_sort.merge_sort(my_list)
    assert my_list == [2, 5, 6, 8]


def test_get_before_in_sorted_permutation():
    a_list = [3, 1, 2, 4, 7]
    ret = utils_sort.get_before_in_sorted_permutation(a_list)
    assert ret == [2, 7, 4, 3, 1]
    a_list = [1, 2, 3, 3, 2, 2, 2]
    ret = utils_sort.get_before_in_sorted_permutation(a_list)
    assert ret == [1, 2, 3, 2, 3, 2, 2]
    a_list = [1, 2, 3]
    ret = utils_sort.get_before_in_sorted_permutation(a_list)
    assert ret == [1, 2, 3]


def test_get_after_in_sorted_permutation():
    a_list = [3, 1, 2, 4, 7]
    ret = utils_sort.get_after_in_sorted_permutation(a_list)
    assert ret == [3, 1, 2, 7, 4]

    a_list = [7, 4, 3, 2, 1]
    ret = utils_sort.get_after_in_sorted_permutation(a_list)
    assert ret == [7, 4, 3, 2, 1]

    a_list = [7, 3, 4, 2, 1]
    ret = utils_sort.get_after_in_sorted_permutation(a_list)
    assert ret == [7, 4, 1, 2, 3]
