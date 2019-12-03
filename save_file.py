import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from pygraphviz import AGraph
import os


def save_graph(file_name, graph, dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    path = os.path.join(dir, file_name)
    dot_path = path + '.dot'
    png_path = path + '.png'
    write_dot(graph, dot_path)
    g = AGraph(dot_path)
    g.draw(png_path, format="png", prog="dot")
