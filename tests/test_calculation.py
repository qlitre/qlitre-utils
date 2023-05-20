from src.qlitreutils import calculation


def test_moving_average():
    temperature = [18, 20, 22, 24, 20]
    results = calculation.moving_average(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]


def test_moving_average_for_loop():
    temperature = [18, 20, 22, 24, 20]
    results = calculation.moving_average_for_loop(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]


def test_get_sum_of_product_pairs():
    numbers = [1, 2, 3]
    assert calculation.get_sum_of_product_pairs(numbers) == 11
    numbers = [1, 3, 5]
    assert calculation.get_sum_of_product_pairs(numbers) == 23


def test_generate_accumulate_in_section():
    a_list = [1, 2, 3, 4, 5]
    section_length = 3
    ret_list = [val for val in calculation.generate_accumulate_in_section(a_list, section_length)]
    assert ret_list == [6, 9, 12]
    a_list = [1, 2, 3, 4, 5]
    section_length = 4
    ret_list = [val for val in calculation.generate_accumulate_in_section(a_list, section_length)]
    assert ret_list == [10, 14]


def test_get_all_sum_pair_in_list():
    a_list = [1, 2, 3, 4, 5]
    target = 5
    ret = calculation.get_all_sum_pair_in_list(a_list, target)
    assert [1, 4] in ret
    assert [2, 3] in ret


def test_count_sum_pairs():
    # 例: n=5, k=7
    assert calculation.count_sum_pairs(5, 7) == 4
    # (1, 6), (2, 5), (3, 4), (4, 3) の4組が条件を満たす

    # 例: n=10, k=12
    assert calculation.count_sum_pairs(10, 12) == 9
    # (1, 11), (2, 10), (3, 9), ..., (9, 3), (10, 2) の9組が条件を満たす

    # 例: n=8, k=5
    assert calculation.count_sum_pairs(8, 5) == 4
    # (1, 4), (2, 3), (3, 2), (4, 1) の4組が条件を満たす

    # 例: n=3, k=3
    assert calculation.count_sum_pairs(3, 3) == 2
    # (1, 2), (2, 1) の2組が条件を満たす

    # 例: n=1, k=1
    assert calculation.count_sum_pairs(1, 1) == 0
    # 条件を満たす組が存在しないため、0を返す

    # 例: n=6, k=11
    assert calculation.count_sum_pairs(6, 11) == 2
    # (5, 6), (6, 5) の2組が条件を満たす
