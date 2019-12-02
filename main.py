from flow_network_generator import *
from max_flow import *
from save_file import *
import os
import argparse

def run_program(n_graph=10):

    gen = FlowNetworkGenerator()
    solver = Max_Flow_Generator()
    for i in range(n_graph):
        # Generate graph and save files
        graph = gen.generate(1, file_name='graph_{}'.format(i + 1))
        residual = generate_residual_graph(graph)
        sink = len(graph)
        max_, res_graph = solver.solve(residual, graph, 1, sink)
        # Save solutions
        save_graph(file_name='graph_{}'.format(i + 1),
                   graph=res_graph,
                   dir=os.path.join(os.getcwd(), 'output_graphs'),
                   attributes=None)

if __name__=="__main__":

    parser = argparse.ArgumentParser(description="How many flow networks do you want to generate and solve?")
    parser.add_argument()


