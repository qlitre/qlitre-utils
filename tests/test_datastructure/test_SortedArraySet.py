from src.qlitreutils.datastructure.SotedArraySet import SortedArraySet


def test_init():
    s = SortedArraySet([3, 1, 2], 'int')
    assert list(s.arr) == [1, 2, 3]
    assert s.a_set == {1, 2, 3}


def test_add():
    s = SortedArraySet([3, 1, 2], 'int')
    s.add(4)
    assert list(s.arr) == [1, 2, 3, 4]
    assert s.a_set == {1, 2, 3, 4}
    s.add(2)  # すでに存在する値を追加
    assert list(s.arr) == [1, 2, 3, 4]  # 重複は許可されない
    assert s.a_set == {1, 2, 3, 4}  # 重複は許可されない


def test_discard():
    s = SortedArraySet([3, 1, 2], 'int')
    s.discard(1)
    assert list(s.arr) == [2, 3]
    assert s.a_set == {2, 3}
    s.discard(5)  # 存在しない値を削除
    assert list(s.arr) == [2, 3]  # エラーなし
    assert s.a_set == {2, 3}  # エラーなし


def test_lt():
    s = SortedArraySet([3, 1, 2], 'int')
    assert s.lt(2) == 1
    assert s.lt(1) is None


def test_le():
    s = SortedArraySet([3, 1, 2], 'int')
    assert s.le(2) == 2
    assert s.le(1) == 1
    assert s.le(0) is None


def test_gt():
    s = SortedArraySet([3, 1, 2], 'int')
    assert s.gt(2) == 3
    assert s.gt(3) is None


def test_ge():
    s = SortedArraySet([3, 1, 2], 'int')
    assert s.ge(2) == 2
    assert s.ge(3) == 3
    assert s.ge(4) is None


def test_init_float():
    s = SortedArraySet([3.1, 1.1, 2.1], 'float')
    assert list(s.arr) == [1.1, 2.1, 3.1]
    assert s.a_set == {1.1, 2.1, 3.1}


def test_add_float():
    s = SortedArraySet([3.1, 1.1, 2.1], 'float')
    s.add(4.1)
    assert list(s.arr) == [1.1, 2.1, 3.1, 4.1]
    assert s.a_set == {1.1, 2.1, 3.1, 4.1}


def test_discard_float():
    s = SortedArraySet([3.1, 1.1, 2.1], 'float')
    s.discard(1.1)
    assert list(s.arr) == [2.1, 3.1]
    assert s.a_set == {2.1, 3.1}


def test_lt_float():
    s = SortedArraySet([3.1, 1.1, 2.1], 'float')
    assert s.lt(2.1) == 1.1
    assert s.lt(1.1) is None


def test_le_float():
    s = SortedArraySet([3.1, 1.1, 2.1], 'float')
    assert s.le(2.1) == 2.1
    assert s.le(1.1) == 1.1
    assert s.le(0.1) is None


def test_gt_float():
    s = SortedArraySet([3.1, 1.1, 2.1], 'float')
    assert s.gt(2.1) == 3.1
    assert s.gt(3.1) is None


def test_ge_float():
    s = SortedArraySet([3.1, 1.1, 2.1], 'float')
    assert s.ge(2.1) == 2.1
    assert s.ge(3.1) == 3.1
    assert s.ge(4.1) is None


def test_init_str():
    s = SortedArraySet(['c', 'a', 'b'], 'str')
    assert list(s.arr) == ['a', 'b', 'c']
    assert s.a_set == {'a', 'b', 'c'}


def test_add_str():
    s = SortedArraySet(['c', 'a', 'b'], 'str')
    s.add('d')
    assert list(s.arr) == ['a', 'b', 'c', 'd']
    assert s.a_set == {'a', 'b', 'c', 'd'}


def test_discard_str():
    s = SortedArraySet(['c', 'a', 'b'], 'str')
    s.discard('a')
    assert list(s.arr) == ['b', 'c']
    assert s.a_set == {'b', 'c'}


def test_lt_str():
    s = SortedArraySet(['c', 'a', 'b'], 'str')
    assert s.lt('b') == 'a'
    assert s.lt('a') is None


def test_le_str():
    s = SortedArraySet
    s = SortedArraySet(['c', 'a', 'b'], 'str')
    assert s.le('b') == 'b'
    assert s.le('a') == 'a'
    assert s.le('@') is None


def test_gt_str():
    s = SortedArraySet(['c', 'a', 'b'], 'str')
    assert s.gt('b') == 'c'
    assert s.gt('c') is None


def test_ge_str():
    s = SortedArraySet(['c', 'a', 'b'], 'str')
    assert s.ge('b') == 'b'
    assert s.ge('c') == 'c'
    assert s.ge('d') is None
