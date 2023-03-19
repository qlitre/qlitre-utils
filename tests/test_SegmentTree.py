from src.qlitreutils.SegmentTree import SegTree


def test_seg_tree():
    # init test
    init_val = [1, 2, 3, 4, 5]
    seg_tree = SegTree(init_val, 'rsq')
    assert seg_tree.query(0, 5) == 15
    assert seg_tree.query(1, 4) == 9

    # update test
    seg_tree.update(2, 10)
    assert seg_tree.query(0, 5) == 22
    assert seg_tree.query(1, 4) == 16

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
