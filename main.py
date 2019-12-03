from flow_network_generator import *
from max_flow import *
from save_file import *
import os
import argparse
import matplotlib.pyplot as plt

def run_program(n_graph=10):

    gen = FlowNetworkGenerator()
    solver = Max_Flow_Generator()
    for i in range(n_graph):
        # Generate graph and save files
        plt.close()
        graph = gen.generate(1, file_name='graph_{}'.format(i + 1))
        residual = generate_residual_graph(graph)
        plt.close()
        sink = len(graph)
        max_, res_graph = solver.solve(residual, graph, 1, sink)
        # Save solutions
        try:
            save_graph(file_name='graph_{}'.format(i + 1),
                       graph=res_graph,
                       dir=os.path.join(os.getcwd(), 'output_graphs'),
                       attributes=None)


        except RuntimeError:
            continue

if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--ngraphs", type=int,
                        help="Enter the number of graphs here")
    args = parser.parse_args()
    if args.ngraphs:
        run_program(args.ngraphs)
    else:
        run_program()

