from src.qlitreutils.helper import unionfind


def test_unionfind():
    n = 6
    uf = unionfind.UnionFind(n)
    assert uf.parents == [-1] * n
    assert uf.group_count() == 6
    uf.union(1, 2)
    uf.union(3, 4)
    assert uf.members(1) == [1, 2]
    assert uf.members(2) == [1, 2]
    assert uf.members(3) == [3, 4]
    assert uf.members(4) == [3, 4]
    assert uf.group_count() == 4
    uf.union(5, 1)
    assert uf.members(1) == [1, 2, 5]
    assert uf.members(2) == [1, 2, 5]
    assert uf.members(5) == [1, 2, 5]
    assert uf.members(3) == [3, 4]
    assert uf.members(4) == [3, 4]
    assert uf.roots() == [0, 1, 3]
    assert uf.size(3) == 2
    assert uf.size(1) == 3
    assert uf.same(3, 4)
    assert uf.same(1, 5)
    assert uf.find(4) == 3
    assert uf.find(5) == 1
    assert uf.all_group_members() == {0: [0], 1: [1, 2, 5], 3: [3, 4]}
