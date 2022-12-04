from src.qlitreutils.helper import unionfind


def test_unionfind_simple():
    n = 6
    uf_simple = unionfind.UnionFindSimple(n)
    assert uf_simple.parents == [-1] * n
    assert uf_simple.group_count() == 6
    uf_simple.union(1, 2)
    uf_simple.union(3, 4)
    assert uf_simple.members(1) == [1, 2]
    assert uf_simple.members(2) == [1, 2]
    assert uf_simple.members(3) == [3, 4]
    assert uf_simple.members(4) == [3, 4]
    assert uf_simple.group_count() == 4
    uf_simple.union(5, 1)
    assert uf_simple.members(1) == [1, 2, 5]
    assert uf_simple.members(2) == [1, 2, 5]
    assert uf_simple.members(5) == [1, 2, 5]
    assert uf_simple.members(3) == [3, 4]
    assert uf_simple.members(4) == [3, 4]
    assert uf_simple.roots() == [0, 1, 3]
    assert uf_simple.size(3) == 2
    assert uf_simple.size(1) == 3
    assert uf_simple.same(3, 4)
    assert uf_simple.same(1, 5)
    assert uf_simple.find(4) == 3
    assert uf_simple.find(5) == 1
    assert uf_simple.all_group_members() == {0: [0], 1: [1, 2, 5], 3: [3, 4]}


def test_unionfind_multiple():
    uf_multi = unionfind.UnionFindMultiple()
    item1 = (1, 1)
    item2 = (1, 2)
    uf_multi.union(item1, item2)
    members = uf_multi.all_group_members()
    assert members == {(1, 1): {(1, 1), (1, 2)}}
    item1 = (1, 1)
    item2 = (3, 3)
    uf_multi.union(item1, item2)
    assert members == {(1, 1): {(1, 1), (1, 2), (3, 3)}}
