from src.qlitreutils import utils_calculation


def test_moving_average():
    temperature = [18, 20, 22, 24, 20]
    results = utils_calculation.moving_average(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]


def test_moving_average_for_loop():
    temperature = [18, 20, 22, 24, 20]
    results = utils_calculation.moving_average_for_loop(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]


def test_get_sum_of_product_pairs():
    numbers = [1, 2, 3]
    assert utils_calculation.get_sum_of_product_pairs(numbers) == 11
    numbers = [1, 3, 5]
    assert utils_calculation.get_sum_of_product_pairs(numbers) == 23


def test_generate_accumulate_in_section():
    a_list = [1, 2, 3, 4, 5]
    section_length = 3
    ret_list = [val for val in utils_calculation.generate_accumulate_in_section(a_list, section_length)]
    assert ret_list == [6, 9, 12]
    a_list = [1, 2, 3, 4, 5]
    section_length = 4
    ret_list = [val for val in utils_calculation.generate_accumulate_in_section(a_list, section_length)]
    assert ret_list == [10, 14]


def test_get_all_sum_pair_in_list():
    a_list = [1, 2, 3, 4, 5]
    target = 5
    ret = utils_calculation.get_all_sum_pair_in_list(a_list, target)
    assert [1, 4] in ret
    assert [2, 3] in ret
