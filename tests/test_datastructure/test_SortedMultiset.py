from src.qlitreutils.datastructure.SortedMultiset import SortedMultiset


def test_add_and_count():
    s = SortedMultiset()
    s.add(1)
    s.add(2)
    s.add(2)
    s.add(3)
    assert s.count(1) == 1
    assert s.count(2) == 2
    assert s.count(3) == 1
    assert s.count(4) == 0


def test_discard():
    s = SortedMultiset([1, 2, 2, 3])
    assert s.discard(2)
    assert s.count(2) == 1
    assert s.discard(2)
    assert s.count(2) == 0
    assert not s.discard(2)
    assert s.count(3) == 1


def test_index_and_iteration():
    s = SortedMultiset([1, 2, 2, 3])
    assert s.index(2) == 1
    assert s.index_right(2) == 3
    assert list(s) == [1, 2, 2, 3]
    assert list(reversed(s)) == [3, 2, 2, 1]


def test_comparison_methods():
    s = SortedMultiset([1, 2, 2, 3])
    assert s.lt(2) == 1
    assert s.lt(1) is None
    assert s.le(2) == 2
    assert s.le(0) is None
    assert s.gt(2) == 3
    assert s.gt(3) is None
    assert s.ge(2) == 2
    assert s.ge(4) is None
