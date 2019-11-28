import matplotlib.pyplot as plt
import networkx as nx
import pygraphviz
from networkx.drawing.nx_agraph import write_dot
import os

def save_graph(file_name, graph, dir, attributes, sep='/'):

    graph_label = None
    if isinstance(attributes, list):
        ls = []
        for i in attributes:
            labels = nx.get_edge_attributes(graph, i)
            ls.append(labels)

        labels = list(zip(*ls))
        graph_label = [sep.join(list(i)) for i in labels]

    else:
        graph_label = nx.get_edge_attributes(graph, attributes)

    pos = nx.random_layout(graph)
    nx.draw(graph, with_labels=True, pos=pos)
    nx.draw_networkx_edge_labels(graph, pos=pos, labels=graph_label)
    path = os.path.join(dir, file_name)
    plt.savefig(path + 'png', format="PNG")
    write_dot(graph, path + 'txt')