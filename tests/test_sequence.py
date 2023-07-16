from src.qlitreutils.sequence import (gen_seq_within_sum_limit_and_length, gen_increasing_seq, find_all_groupings,
                                      generate_pairs)
import pytest


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


def test_find_all_groupings():
    def sorted_groupings(groupings):
        return sorted(sorted(group) for group in groupings)

    # テストケース1: 2人の選手を2つのグループに分ける
    result1 = find_all_groupings(0, [], 2, 2)
    expected1 = [[{0}, {1}]]
    assert sorted(result1) == sorted(expected1)

    # テストケース2: 3人の選手を2つのグループに分ける
    result2 = find_all_groupings(0, [], 3, 2)
    expected2 = [[{0, 1}, {2}], [{0, 2}, {1}], [{0}, {1, 2}]]
    assert sorted(result2) == sorted(expected2)

    # テストケース3: 3人の選手を3つのグループに分ける
    result3 = find_all_groupings(0, [], 3, 3)
    expected3 = [[{0}, {1}, {2}]]
    assert sorted(result3) == sorted(expected3)

    # テストケース4: 4人の選手を2つのグループに分ける
    result4 = find_all_groupings(0, [], 4, 2)
    expected4 = [[{0, 1, 2}, {3}], [{0, 1, 3}, {2}], [{0, 1}, {2, 3}], [{0, 2, 3}, {1}], [{0, 2}, {1, 3}],
                 [{0, 3}, {1, 2}], [{0}, {1, 2, 3}]]
    assert sorted(result4) == sorted(expected4)


def test_generate_pairs():
    # 入力が2つの要素のみを含むリストの場合
    assert generate_pairs(['A', 'B']) == [[('A', 'B')]]

    # 入力が4つの要素を含むリストの場合
    assert generate_pairs(['A', 'B', 'C', 'D']) == [
        [('A', 'B'), ('C', 'D')],
        [('A', 'C'), ('B', 'D')],
        [('A', 'D'), ('B', 'C')]
    ]

    # 入力が空のリストの場合
    assert generate_pairs([]) == []

    # 入力が1つの要素を含むリストの場合
    assert generate_pairs(['A']) == []


@pytest.mark.parametrize('lst', [
    ['A', 'B', 'C'],
    ['A', 'B', 'C', 'D', 'E'],
    ['A', 'B', 'C', 'D', 'E', 'F']
])
def test_generate_pairs_length(lst):
    # 全ての出力がlen(lst) // 2 長のタプルのリストであることを確認
    for pairs in generate_pairs(lst):
        assert all(len(pair) == 2 for pair in pairs)
        assert len(pairs) == len(lst) // 2
