import networkx as nx
import copy
import queue
import math

class Max_Flow_Generator():
    def __init__(self, G):
        self.G = G


    def solve(self, source, sink):
        f = 0

        while True:
            q = queue.Queue()
            q.put(source)

            pred = [None]*(len(self.G) + 1)
            # while the queue is not empty
            while not q.empty():
                curr = q.get()

                for e in self.G.neighbors(curr):
                    if pred[e] is None and e != source and self.G[curr][e]['cap'] > self.G[curr][e]['flow']:
                        pred[e] = {'source': curr, 'sink': e,
                                   'cap': self.G[curr][e]['cap'], 'flow': self.G[curr][e]['flow']}
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
                    self.G[s][t]['flow'] += df
                    self.G[t][s]['flow'] -= df

                f += df

        return f
