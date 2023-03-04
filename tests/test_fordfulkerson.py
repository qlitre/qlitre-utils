from src.qlitreutils import fordfulkerson


def test_fordfulkerson():
    n = 6
    edge = [
        [1, 2, 5],
        [1, 4, 4],
        [2, 3, 4],
        [2, 5, 7],
        [3, 6, 3],
        [4, 5, 3],
        [5, 6, 5]
    ]
    ff = fordfulkerson.FordFulkerson(n)
    for a, b, c in edge:
        ff.add_edge(a - 1, b - 1, c)
    assert ff.flow(0, n - 1) == 8
