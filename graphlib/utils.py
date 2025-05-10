from graphlib.core import Graph

def graph_info_file(graph: Graph, file_name: str=None) -> None:
    if file_name == None:
        file_name = graph.title
    file_name = file_name.replace(" ", "_")  + ".txt"

    with open(file_name, 'w') as fd:
        fd.write(str(graph))