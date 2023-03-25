from src.qlitreutils.SegmentTree import SegTree


def test_seg_tree():
    # init test
    init_val = [1, 2, 3, 4, 5]
    seg_tree = SegTree(init_val, 'rsq')
    assert seg_tree.query(0, 5) == 15
    assert seg_tree.query(1, 4) == 9

    # update test
    init_val = [1, 3, 5, 7, 9, 11]
    seg_tree = SegTree(init_val, mode='rsq')
    seg_tree.update(3, 10)
    assert seg_tree.select(3) == 10
    assert seg_tree.query(0, 6) == sum([1, 3, 5, 10, 9, 11])
    seg_tree.update(2, 2)
    assert seg_tree.select(2) == 2
    assert seg_tree.query(0, 6) == sum([1, 3, 2, 10, 9, 11])
    seg_tree.update(5, 0)
    assert seg_tree.select(5) == 0
    assert seg_tree.query(0, 6) == sum([1, 3, 2, 10, 9, 0])

    # selectのテスト
    init_val = [1, 3, 5, 7, 9, 11]
    seg_tree = SegTree(init_val, mode='rsq')
    assert seg_tree.select(0) == init_val[0]
    assert seg_tree.select(3) == init_val[3]
    assert seg_tree.select(5) == init_val[5]

    # query test
    init_val = [5, 4, 3, 2, 1]
    seg_tree = SegTree(init_val, 'rmiq')
    assert seg_tree.query(0, 5) == 1
    assert seg_tree.query(1, 4) == 2

    init_val = [5, 4, 3, 2, 1]
    seg_tree = SegTree(init_val, 'rmaq')
    assert seg_tree.query(0, 5) == 5
    assert seg_tree.query(1, 4) == 4

    init_val = [1, 2, 3, 4, 5]
    seg_tree = SegTree(init_val, 'rsq')
    assert seg_tree.query(0, 5) == 15
    assert seg_tree.query(1, 4) == 9

    init_val = [1, 2, 3, 4, 5]
    seg_tree = SegTree(init_val, 'rpq')
    assert seg_tree.query(0, 5) == 120
    assert seg_tree.query(1, 4) == 24

    init_val = [12, 18, 9, 21, 6]
    seg_tree = SegTree(init_val, 'rgcdq')
    assert seg_tree.query(0, 5) == 3
    assert seg_tree.query(1, 4) == 3

    # 区間xor和のテスト
    init_val = [0b110, 0b101, 0b010, 0b001]
    seg_tree = SegTree(init_val, mode='rxorsq')
    assert seg_tree.query(0, 4) == (0b110 ^ 0b101 ^ 0b010 ^ 0b001)
    assert seg_tree.query(1, 3) == (0b101 ^ 0b010)
    assert seg_tree.query(2, 4) == (0b010 ^ 0b001)
