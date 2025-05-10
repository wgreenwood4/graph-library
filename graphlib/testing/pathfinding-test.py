import sys
from graphlib.core import Graph
from graphlib.extras import pathfinding
from graphlib.extras import visuals
from graphlib.utils import graph_info_file

"""
Graph used for testing comes from:
  https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""

def di_graph() -> Graph:
    g = Graph(title="Dijkstra Test", directed=False, weighted=True)

    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 3, 7)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)

    g.add_edge(1, 7, 11)
    g.add_edge(1, 2, 8)

    

    g.add_edge(3, 5, 14)
    g.add_edge(3, 4, 9)

    g.add_edge(4, 5, 10)

    g.add_edge(5, 6, 2)

    g.add_edge(6, 8, 6)
    g.add_edge(6, 7, 1)

    g.add_edge(7, 8, 7)

    return g

def bm_graph() -> Graph:
    g = Graph(title="Bellman-Ford Test", directed=True, weighted=True)

    for i in range(0, 4 + 1):
        g.add_node(i)

    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 4, 1)
    g.add_edge(4, 3, -1)

    return g

def fw_graph() -> Graph:
    # https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

    g = Graph(title="Floyd-Warshall Test", directed=True, weighted=True)

    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')

    g.add_edge('A', 'D', 5)
    g.add_edge('A', 'B', 4)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'E', 6)
    g.add_edge('C', 'A', 2)
    g.add_edge('C', 'D', 3)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'C', 1)
    g.add_edge('E', 'A', 1)
    g.add_edge('E', 'D', 4)

    return g

def negative_cycle() -> Graph:
    g = Graph(title="Negative Cycle", directed=True, weighted=True)

    for i in range(0, 3 + 1):
        g.add_node(i)

    g.add_edge(0, 1, 4)
    g.add_edge(3, 1, -2)
    g.add_edge(1, 2, -6)
    g.add_edge(2, 3, 5)

    return g

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Enter flag: d | bm | fw | other")
        exit(1)

    if sys.argv[1] == 'd':
        print("Dijkstra's Algorithm:")
        dijkstra_graph = di_graph()
        d_spt, d_distances = pathfinding.dijkstra(dijkstra_graph, 0)
        print("Shortest path tree:")
        for key, value in d_spt.adj_list.items():
            print(f"{key}: {value}")
        print("\nDistances:")
        for key, value in d_distances.items():
            print(f"{key}: {value}")
        visuals.draw_graph(dijkstra_graph)
        visuals.draw_graph(d_spt)

    elif sys.argv[1] == 'bm':
        print("Bellman-Ford Algorithm:")
        bellman_ford_graph = bm_graph()
        bm_spt, bm_distances = pathfinding.bellman_ford(bellman_ford_graph, 0)
        print("Shortest path tree:")
        for key, value in bm_spt.adj_list.items():
            print(f"{key}: {value}")
        print("\nDistances:")
        for key, value in bm_distances.items():
            print(f"{key}: {value}")
        visuals.draw_graph(bellman_ford_graph)
        visuals.draw_graph(bm_spt)

    elif sys.argv[1] == 'fw':
        print("Floyd-Warshall Algorithm:")
        floyd_warshall_graph = fw_graph()
        fw_distances = pathfinding.floyd_warshall(floyd_warshall_graph)
        for row in fw_distances:
            print(*row, sep="\t")
        visuals.draw_graph(floyd_warshall_graph)
    
    elif sys.argv[1] == 'other':
        graph = di_graph()
        print(graph)
        graph_info_file(graph)