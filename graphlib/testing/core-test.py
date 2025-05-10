from graphlib.core import Graph

# Create a new graph instance
graph = Graph("Test Graph", directed=False, weighted=True)

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")

# Construction testing
print("Nodes:", graph.nodes)

graph.add_edge("A", "B", 3)
graph.add_edge("A", "C", 2)

# Structures testing
print("Adjacency list:", graph.adj_list)

adj_matrix = graph.get_adj_matrix()
print("Adjacency matrix", adj_matrix)

edge_list = graph.get_edge_list()
print("Edge list", edge_list)

# Helpers testing
print("Order", graph.order())

print("Has node A:", graph.has_node("A")) # True
print("Has node D:", graph.has_node("D")) # False

print("Has edge A, B:", graph.has_edge("A", "B")) # True
print("Has edge B, C:", graph.has_edge("B", "C")) # False
print("Has edge B, A:", graph.has_edge("B", "C")) # False

print("Degree of A:", graph.degree("A")) # 2
print("Degree of B:", graph.degree("B")) # 0

print("Neighbors of A:", graph.get_neighbors("A")) # ["B", "C"]

print("Weight of edge A, C:", graph.get_weight("A", "C"))


