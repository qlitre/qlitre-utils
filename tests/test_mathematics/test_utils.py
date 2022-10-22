from src.qlitreutils.mathematics import utils


def test_base_10_to_base_n():
    num_10 = 8
    assert utils.base_10_to_base_n(num_10, 2) == 1000

    num_10 = 10
    assert utils.base_10_to_base_n(num_10, 3) == 101


def test_base_n_to_base_10():
    num_2 = 1000
    assert utils.base_n_to_base_10(num_2, 2) == 8
    num_3 = 101
    assert utils.base_n_to_base_10(num_3, 3) == 10
