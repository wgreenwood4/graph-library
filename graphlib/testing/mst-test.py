from graphlib.core import Graph
from graphlib.extras import mst, visuals

"""
Graph used for testing comes from:
  https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""

def make_graph() -> Graph:
    g = Graph(title="MST Test", directed=False, weighted=True)

    for i in range(0, 8 + 1):
        g.add_node(i)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)

    g.add_edge(1, 7, 11)
    g.add_edge(1, 2, 8)

    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 3, 7)

    g.add_edge(3, 5, 14)
    g.add_edge(3, 4, 9)

    g.add_edge(4, 5, 10)

    g.add_edge(5, 6, 2)

    g.add_edge(6, 8, 6)
    g.add_edge(6, 7, 1)

    g.add_edge(7, 8, 7)

    return g

if __name__ == "__main__":
    graph = make_graph()
    # visuals.draw_graph(graph)

    print("Kruskal's Algorithm:")
    kruskal_mst = mst.kruskal(graph, verbose=True)
    visuals.draw_graph(kruskal_mst)

    print("\nPrim's Algorithm:")
    prim_mst = mst.prim(graph, verbose=True)
    # visuals.draw_graph(prim_mst)
    
