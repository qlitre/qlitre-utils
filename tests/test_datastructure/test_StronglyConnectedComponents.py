import pytest
from src.qlitreutils.datastructure.StronglyConnectedComponents import StronglyConnectedComponents


def test_disconnected_nodes():
    scc = StronglyConnectedComponents(3)
    scc.build()
    _, groups = scc.construct()
    assert sorted(groups) == [[0], [1], [2]]


def test_linear_graph():
    scc = StronglyConnectedComponents(3)
    scc.add_edge(0, 1)
    scc.add_edge(1, 2)
    scc.build()
    dag, groups = scc.construct()
    assert sorted(groups) == [[0], [1], [2]]
    # DAGの構造についての具体的なアサーションは実装によって異なる


def test_cycle_graph():
    scc = StronglyConnectedComponents(3)
    scc.add_edge(0, 1)
    scc.add_edge(1, 2)
    scc.add_edge(2, 0)
    scc.build()
    dag, groups = scc.construct()
    assert groups == [[0, 1, 2]]  # DAGが空か単一の空リストを含むかは実装による


def test_complex_graph():
    scc = StronglyConnectedComponents(4)
    scc.add_edge(0, 1)
    scc.add_edge(1, 2)
    scc.add_edge(2, 1)
    scc.add_edge(2, 3)
    scc.build()
    dag, groups = scc.construct()
    assert len(groups) == 3
