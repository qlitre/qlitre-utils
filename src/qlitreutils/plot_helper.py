import networkx as nx
import matplotlib.pyplot as plt


def plot_graph_by_dict(data: dict, n: int, start_one: bool = True, directed: bool = False):
    """
    辞書を元に無向グラフを可視化する
    """
    if directed:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

    for i in range(n):
        if start_one:
            graph.add_node(i + 1)
        else:
            graph.add_node(i)
    for node, edges in data.items():
        for edge in edges:
            graph.add_edge(node, edge)
    fig, ax = plt.subplots()
    nx.draw(graph, with_labels=True)
    fig.tight_layout()
    plt.show()


def plot_graph_by_connected_list(data: list, n: int, start_one: bool = True, directed: bool = False):
    """
    連結リストを元に無向グラフを可視化する
    """
    if directed:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

    for i in range(n):
        if start_one:
            graph.add_node(i + 1)
        else:
            graph.add_node(i)
    for node in range(len(data)):
        for edge in data[node]:
            graph.add_edge(node, edge)

    fig, ax = plt.subplots()
    nx.draw(graph, with_labels=True)
    fig.tight_layout()
    plt.show()


def job():
    n = 8
    # 辞書型の場合
    d = {1: [3, 5, 2, 4],
         2: [6, 4, 1, 7, 5, 3, 8],
         3: [1, 8, 6, 4, 5, 2, 7],
         4: [7, 6, 3, 2, 1, 5],
         5: [6, 1, 3, 2, 4, 7],
         7: [4, 2, 3, 6, 5],
         6: [2, 5, 3, 4, 7],
         8: [3, 2]}
    plot_graph_by_dict(d, n, directed=False)
    n = 5
    # 連結リストの場合
    d = [[], [2], [1], [1], [5], [4]]
    plot_graph_by_connected_list(d, n, directed=True)


if __name__ == '__main__':
    job()
