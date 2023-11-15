from src.qlitreutils.datastructure.UnionFindPotential import UnionFindPotential


def test_initialization():
    uf = UnionFindPotential(10)
    assert len(uf.parent) == 10
    assert all(rank == 0 for rank in uf.rank)
    assert all(diff == 0 for diff in uf._diff)


def test_union_find():
    uf = UnionFindPotential(10)
    assert uf.union(0, 1, 5)
    assert uf.find(0) == uf.find(1)
    assert uf.union(1, 2, 3)
    assert uf.find(0) == uf.find(2)


def test_same():
    uf = UnionFindPotential(10)
    uf.union(0, 1, 5)
    assert uf.same(0, 1)
    assert not uf.same(0, 2)


def test_diff():
    uf = UnionFindPotential(10)
    uf.union(0, 1, 5)
    uf.union(1, 2, 3)
    assert uf.diff(0, 2) == 8
    assert uf.diff(2, 0) == -8


def test_union_consistency():
    uf = UnionFindPotential(10)
    uf.union(0, 1, 5)
    uf.union(1, 2, 3)
    uf.union(0, 2, 8)
    assert uf.find(0) == uf.find(2)
    assert uf.diff(0, 2) == 8
