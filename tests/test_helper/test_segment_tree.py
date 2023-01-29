from src.qlitreutils.helper import segment_tree


def test_seg_tree():
    a_list = [1, 2, 3, 4, 5, 6, 7]
    seg = segment_tree.SegTree(a_list, mode='rsq')
    res = seg.query(0, 7)
    assert res == 28
    res = seg.query(1, 3)
    assert res == 5
    res = seg.query(2, 3)
    assert res == 3
    seg.update(1, 5)
    res = seg.query(1, 3)
    assert res == 8
