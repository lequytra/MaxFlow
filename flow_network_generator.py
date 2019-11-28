from random import randrange
from random import choice
from networkx import DiGraph
from networkx.drawing.nx_pydot import write_dot
from pygraphviz import AGraph


class FlowNetworkGenerator:
    def __init__(self, min_nodes=5, max_nodes=15, max_weight=20):
        self.minNodes = min_nodes
        self.maxNodes = max_nodes
        self.maxWeight = max_weight

    def generate_flow(self):
        graph = DiGraph()
        source = 1
        sink = randrange(self.minNodes, self.maxNodes+1, 1)  # sink is last node
        # max edges: n-1 nodes sending edges, each can send to n-1-1 nodes because can't send to source or self.
        # source already considers itself, so it can send to n-1 nodes, so add 1 edge.
        min_edges = sink - 1
        max_edges = (sink - 1) * (sink - 2) + 1
        edges = randrange(min_edges, max_edges+1, 1)
        unvisited = list(range(source, sink+1))

        # keep track of valid edges
        edge_list = []
        for a in range(1, sink):
            for b in range(2, sink+1):
                if b != a:
                    edge_list.append([a, b])

        graph.add_nodes_from(unvisited)
        graph.add_node(source, label="source")
        graph.add_node(sink, label="sink")
        unvisited.remove(sink)
        unvisited.remove(source)

        current_node = source
        next_node = 0
        # loop to generate path connecting all nodes
        while len(unvisited) > 0:
            next_node = choice(unvisited)
            unvisited.remove(next_node)
            graph.add_edge(current_node, next_node, label=randrange(1, self.maxWeight, 1))
            edge_list.remove([current_node, next_node]) # remove list from valid edges
            current_node = next_node

        graph.add_edge(current_node, sink, label=randrange(1, self.maxWeight, 1))
        while graph.size() < edges and len(edge_list) > 0:
            edge = choice(edge_list)  # extract random valid edge
            edge_list.remove(edge)
            graph.add_edge(edge[0], edge[1], label=randrange(1, self.maxWeight, 1))
        return graph

    def generate(self, num):
        for i in range(1, num + 1):
            flow = self.generate_flow()
            write_dot(flow, "graph" + str(i) + ".dot")
            g = AGraph("graph" + str(i) + ".dot")
            g.draw("graph" + str(i) + ".png", format="png", prog="dot")


gen = FlowNetworkGenerator()
graph_num = 5
gen.generate(graph_num)
