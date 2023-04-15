from src.qlitreutils.datastructure.SortedSet import SortedSet


def test_init():
    s = SortedSet()
    assert len(s) == 0

    s = SortedSet([3, 2, 1])
    assert len(s) == 3
    assert list(s) == [1, 2, 3]


def test_add():
    s = SortedSet([1, 3, 5])
    assert s.add(4) is True
    assert s.add(4) is False
    assert len(s) == 4
    assert list(s) == [1, 3, 4, 5]


def test_discard():
    s = SortedSet([1, 2, 3])
    assert s.discard(2) is True
    assert s.discard(2) is False
    assert len(s) == 2
    assert list(s) == [1, 3]


def test_contains():
    s = SortedSet([1, 2, 3])
    assert 2 in s
    assert 4 not in s


def test_lt():
    s = SortedSet([1, 3, 5])
    assert s.lt(3) == 1
    assert s.lt(1) is None


def test_le():
    s = SortedSet([1, 3, 5])
    assert s.le(3) == 3
    assert s.le(0) is None


def test_gt():
    s = SortedSet([1, 3, 5])
    assert s.gt(3) == 5
    assert s.gt(5) is None


def test_ge():
    s = SortedSet([1, 3, 5])
    assert s.ge(3) == 3
    assert s.ge(6) is None


def test_index():
    s = SortedSet([1, 2, 3])
    assert s.index(2) == 1
    assert s.index(4) == 3


def test_index_right():
    s = SortedSet([1, 2, 3])
    assert s.index_right(2) == 2
    assert s.index_right(4) == 3
