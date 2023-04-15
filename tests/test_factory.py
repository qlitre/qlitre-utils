from src.qlitreutils.factory import generate_sequences_within_sum_limit_and_length, generate_lunlun_numbers


def test_generate_sequences_within_sum_limit_and_length():
    res = generate_sequences_within_sum_limit_and_length(5, 1, 3)
    expect = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 3, 1], [2, 1, 1], [2, 1, 2], [2, 2, 1],
              [3, 1, 1]]
    assert res == expect


def test_generate_lunlun_numbers():
    # 最初の10個のルンルン数をテスト
    first_10_lunlun_numbers = generate_lunlun_numbers(10)
    assert first_10_lunlun_numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 最初の15個のルンルン数をテスト
    first_20_lunlun_numbers = generate_lunlun_numbers(20)
    assert first_20_lunlun_numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 21, 22, 23, 32, 33, 34, 43, 44]

    # 100000番目のルンルン数をテスト
    lunlun_100000 = generate_lunlun_numbers(100000)[-1]
    assert lunlun_100000 == 3234566667
