from src.qlitreutils.datastructure.SortedArrayMultiSet import SortedArrayMultiSet


def test_sorted_array_multiset():
    s = SortedArrayMultiSet([3, 1, 2, 2, 3, 4])

    assert s.arr.tolist() == [1, 2, 2, 3, 3, 4]

    s.add(5)
    assert s.arr.tolist() == [1, 2, 2, 3, 3, 4, 5]

    s.add(2)
    assert s.arr.tolist() == [1, 2, 2, 2, 3, 3, 4, 5]

    s.discard(2)
    assert s.arr.tolist() == [1, 2, 2, 3, 3, 4, 5]

    s.discard(5)
    assert s.arr.tolist() == [1, 2, 2, 3, 3, 4]

    assert s.lt(3) == 2
    assert s.le(3) == 3
    assert s.gt(3) == 4
    assert s.ge(3) == 3

    assert not s.lt(1)
    assert s.le(1) == 1
    assert not s.gt(4)
    assert s.ge(4) == 4
