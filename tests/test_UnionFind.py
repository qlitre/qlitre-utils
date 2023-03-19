from src.qlitreutils.UnionFind import UnionFindSimple, UnionFindMultiple


def test_unionfind_simple():
    uf = UnionFindSimple(6)
    uf.union(0, 2)
    uf.union(1, 3)
    uf.union(2, 4)
    assert uf.parents == [-3, -2, 0, 1, 0, -1]
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 0
    assert uf.find(3) == 1
    assert uf.find(4) == 0
    assert uf.same(0, 4)
    assert not uf.same(1, 4)
    assert not uf.same(2, 3)
    assert uf.size(0) == 3
    assert uf.size(1) == 2
    assert uf.size(2) == 3
    assert uf.members(0) == [0, 2, 4]
    assert uf.members(1) == [1, 3]
    assert uf.roots() == [0, 1, 5]


def test_unionfind_multiple():
    uf = UnionFindMultiple()
    assert uf.dict_find((1, 2)) == 1
    assert uf.dict_find((1, 2)) == 1
    assert uf.dict_find("abc") == 2
    assert uf.dict_find((2, 3)) == 3
    assert uf.dict_find((4, 5)) == 4
    assert uf.dict_find((4, 5)) == 4
    assert uf.dict_find("xyz") == 5
    assert uf.parents == {(1, 2): 1, "abc": 2, (2, 3): 3, (4, 5): 4, "xyz": 5}
    uf.union((1, 2), "abc")
    uf.union((4, 5), "xyz")
    uf.union((1, 2), (2, 3))
    assert uf.members((1, 2)) == {(1, 2), "abc", (2, 3)}
    assert uf.members((4, 5)) == {(4, 5), "xyz"}
    assert uf.members("abc") == {(1, 2), (2, 3), "abc"}
    assert uf.members((2, 3)) == {(1, 2), (2, 3), "abc"}
    assert uf.same((1, 2), "abc")
    assert uf.same((1, 2), (2, 3))
    assert not uf.same((1, 2), (4, 5))
    assert uf.group_count() == 2
    assert uf.all_group_members() == {(1, 2): {(1, 2), "abc", (2, 3)}, (4, 5): {(4, 5), "xyz"}}
