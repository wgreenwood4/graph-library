import sys

from graphlib.core import Graph
from graphlib.extras import analysis
from graphlib.extras import traversals as trv


NUM_NODES = 8

def make_graph(t: str="Traversal Graph") -> Graph:
    g = Graph(title=t, directed=False, weighted=False)
    
    for i in range(0, NUM_NODES):
        g.add_node(f"{i}")

    g.add_edge("0", "1")
    g.add_edge("1", "2")
    g.add_edge("2", "3")
    
    g.add_edge("4", "5")
    g.add_edge("5", "6")
    g.add_edge("6", "7")
    g.add_edge("7", "4")

    return g

def test_bfs(g: Graph):
    # Run BFS
    print("BFS Traversal:", trv.bfs_order(g, start="0"))

    print("BFS for:")
    for i in range(0, NUM_NODES + 4):
        print(f"  '{i}':", trv.bfs_contains(g, start="0", target=f"{i}"))

def test_dfs(g: Graph):
    # Run BFS
    print("DFS Traversal:", trv.dfs_order(g, start="0"))

    print("DFS for:")
    for i in range(0, NUM_NODES + 6):
        print(f"  '{i}':", trv.dfs_contains(g, start="0", target=f"{i}"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Provide bfs/dfs option")
        exit(1)

    g = make_graph()

    # BFS/DFS tests
    if sys.argv[1] == "bfs":
        test_bfs(g)
    elif sys.argv[1] == "dfs":
        test_dfs(g)
    
    # Component tests
    components = analysis.get_components(g, sorted=True)
    print("Components:", len(components))
    print(f"  {components}")

    # Cycle tests
    print("Has cycles:", analysis.has_cycles(g))