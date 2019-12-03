import networkx as nx
import copy
import queue
import math
from flow_network_generator import *


class Max_Flow_Generator():
    def __init__(self):
        pass

    def solve(self, G, original_graph, source, sink):
        f = 0

        while True:
            q = queue.Queue()
            q.put(source)
            pred = [None]*(sink + 1)
            # while the queue is not empty
            while not q.empty():
                curr = q.get()

                for e in G.neighbors(curr):

                    if pred[e] is None and e != source and G[curr][e]['cap'] > G[curr][e]['flow']:
                        pred[e] = {'source': curr, 'sink': e,
                                   'cap': G[curr][e]['cap'], 'flow': G[curr][e]['flow']}
                        q.put(e)

            # if no augmenting path is found
            if pred[sink] is None:
                break
            # If we found an augmenting path
            else:
                df = math.inf
                e = pred[sink]
                while e is not None:
                    df = min(df, e['cap'] - e['flow'])
                    e = pred[e['source']]

                # Updates the edges
                e = pred[sink]
                while e is not None:
                    s = e['source']
                    t = e['sink']
                    G[s][t]['flow'] += df
                    try:
                        G[t][s]['flow'] -= df
                        e = pred[e['source']]
                    except KeyError:
                        print("{} {}".format(t, s))
                f += df

        res_graph = self.return_result(G, original_graph)

        return f, res_graph

    def return_result(self, G, original_graph):
        atts = nx.get_edge_attributes(G, 'flow')
        nx.set_edge_attributes(original_graph, atts, 'flow')

        return original_graph
