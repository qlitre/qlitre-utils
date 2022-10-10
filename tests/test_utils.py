from utils import utils


def test_moving_average():
    temperature = [18, 20, 22, 24, 20]
    results = utils.moving_average(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]


def test_moving_average_for_loop():
    temperature = [18, 20, 22, 24, 20]
    results = utils.moving_average_for_loop(temperature, 2)
    assert results == [19.0, 21.0, 23.0, 22.0]
