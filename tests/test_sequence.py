from src.qlitreutils.sequence import gen_seq_within_sum_limit_and_length, gen_increasing_seq


def test_generate_sequences_within_sum_limit_and_length():
    res = gen_seq_within_sum_limit_and_length(5, 1, 3)
    expect = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 3, 1], [2, 1, 1], [2, 1, 2], [2, 2, 1],
              [3, 1, 1]]
    assert res == expect


def test_gen_increasing_seq():
    # Test case 1
    assert gen_increasing_seq(2, 2) == [
        [1, 1],
        [1, 2],
        [2, 2],
    ]

    # Test case 2
    assert gen_increasing_seq(2, 3) == [
        [1, 1],
        [1, 2],
        [1, 3],
        [2, 2],
        [2, 3],
        [3, 3],
    ]

    # Test case 3
    assert gen_increasing_seq(3, 2) == [
        [1, 1, 1],
        [1, 1, 2],
        [1, 2, 2],
        [2, 2, 2],
    ]

    # Test case 4
    assert gen_increasing_seq(1, 3) == [
        [1],
        [2],
        [3],
    ]

    # Test case 5
    assert gen_increasing_seq(3, 1) == [
        [1, 1, 1],
    ]
