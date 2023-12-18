import pytest
from src.qlitreutils.datastructure.SegmentTree import SegTree


# 初期化テスト
def test_seg_tree_initialization():
    init_val = [1, 2, 3, 4, 5]
    seg_tree = SegTree(init_val, 'rsq')
    assert seg_tree.query(0, 5) == 15
    assert seg_tree.query(1, 4) == 9


# 更新テスト
@pytest.mark.parametrize("index, new_value, expected_sum", [
    (3, 10, sum([1, 3, 5, 10, 9, 11])),
    (2, 2, sum([1, 3, 2, 7, 9, 11])),
    (5, 0, sum([1, 3, 2, 10, 9, 0]))
])
def test_seg_tree_update(index, new_value, expected_sum):
    init_val = [1, 3, 5, 7, 9, 11]
    seg_tree = SegTree(init_val, 'rsq')
    seg_tree.update(index, new_value)
    assert seg_tree.query(0, 6) == expected_sum


# selectのテスト
@pytest.mark.parametrize("index, expected_value", [
    (0, 1),
    (3, 7),
    (5, 11)
])
def test_seg_tree_select(index, expected_value):
    init_val = [1, 3, 5, 7, 9, 11]
    seg_tree = SegTree(init_val, 'rsq')
    assert seg_tree.select(index) == expected_value


# クエリテスト
@pytest.mark.parametrize("mode, expected_result", [
    ('rmiq', 1),
    ('rmaq', 5),
    ('rsq', 15),
    ('rpq', 120),
    ('rgcdq', 3),
    ('rxorsq', 0b110 ^ 0b101 ^ 0b010 ^ 0b001)
])
def test_seg_tree_query(mode, expected_result):
    init_val = [5, 4, 3, 2, 1] if mode in ['rmiq', 'rmaq'] else [1, 2, 3, 4, 5]
    init_val = [12, 18, 9, 21, 6] if mode == 'rgcdq' else init_val
    init_val = [0b110, 0b101, 0b010, 0b001] if mode == 'rxorsq' else init_val
    seg_tree = SegTree(init_val, mode)
    if mode == 'rxorsq':
        assert seg_tree.query(0, 4) == expected_result
    else:
        assert seg_tree.query(0, 5) == expected_result
