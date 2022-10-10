from qlitreutils.sort import utils


def test_bubble_sort():
    my_list = [6, 5, 8, 2]
    my_list = utils.bubble_sort(my_list)
    assert my_list == [2, 5, 6, 8]


def test_insertion_sort():
    my_list = [6, 5, 8, 2]
    my_list = utils.insertion_sort(my_list)
    assert my_list == [2, 5, 6, 8]


def test_merge_sort():
    my_list = [6, 5, 8, 2]
    my_list = utils.merge_sort(my_list)
    assert my_list == [2, 5, 6, 8]
