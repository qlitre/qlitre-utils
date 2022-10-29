from src.qlitreutils.calculation import utils


def test_moving_average():
    temperature = [18, 20, 22, 24, 20]
    results = utils.moving_average(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]


def test_moving_average_for_loop():
    temperature = [18, 20, 22, 24, 20]
    results = utils.moving_average_for_loop(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]


def test_get_sum_of_product_pairs():
    numbers = [1, 2, 3]
    assert utils.get_sum_of_product_pairs(numbers) == 11
    numbers = [1, 3, 5]
    assert utils.get_sum_of_product_pairs(numbers) == 23
