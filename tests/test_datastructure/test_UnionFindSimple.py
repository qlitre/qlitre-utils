from src.qlitreutils.datastructure.UnionFindSimple import UnionFindSimple


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



