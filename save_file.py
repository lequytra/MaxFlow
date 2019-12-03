import matplotlib.pyplot as plt
import networkx as nx
import pygraphviz
from networkx.drawing.nx_agraph import write_dot
import os


def save_graph(file_name, graph, dir, attributes=None, sep='/'):

    if not os.path.isdir(dir):
        os.mkdir(dir)

    if attributes is None:
        attributes = ['flow', 'cap']

    if isinstance(attributes, list):
        ls = []
        for i in attributes:
            labels = nx.get_edge_attributes(graph, i)
            ls.append(labels)

        graph_label = {}
        for key, item in ls[0].items():
            graph_label[key] = sep.join([str(d[key]) for d in ls])

    else:
        graph_label = nx.get_edge_attributes(graph, attributes)

    node_labels = nx.get_node_attributes(graph, 'label')

    path = os.path.join(dir, file_name)
    pos = nx.random_layout(graph)
    nx.draw_networkx(graph, with_labels=False, pos=pos)
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=graph_label)
    nx.draw_networkx_labels(graph, pos=pos, labels=node_labels)
    plt.savefig(path + '.png', format="PNG")
    write_dot(graph, path + '.dot')
