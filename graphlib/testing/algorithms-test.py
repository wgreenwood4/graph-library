from graphlib.core import Graph
from graphlib.extras import algorithms, visuals
from graphlib.utils import graph_info_file

if __name__ == "__main__":
    k = algorithms.k_graph(30)
    kib = algorithms.k_bipartite_graph(4, 4)
    c = algorithms.c_graph(2)

    graph = k
    graph_info_file(graph)
    visuals.draw_graph(graph)