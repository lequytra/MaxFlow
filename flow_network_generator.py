# Remember to test connectivity
import networkx as nx

class FlowNetworkGenerator():
    def __init__(self):
        self.G = nx.DiGraph()

    def make_graph(self, n_nodes=10, n_edges=10):
        if n_edges < n_nodes - 1:
            raise Exception("The number of edges must be at least equal to the number"
                            "of nodes - 1 to ensure connectivity.")




