"""
This file contains helper functions for the cse551a3_main.py script where the modified Dijkstra's algorithm
resides.
"""

import networkx as nx
import matplotlib.pyplot as plt
from random import randint, uniform


def cost_f(t, step=10):  # option 1 for stochastic nondecreasing cost function
    return t + round((1 / step) * uniform(t, t + step), 2)


def f_e(t):  # option 2 for stochastic nondecreasing cost function -- simple
    return t + round(uniform(0, 1), 2)


class Graph:

    def __init__(self, digraph):
        """
        :param digraph: dictionary of the form:
            d = {
                    Node v1: [( Connected Node v2, weight = w(v1,v2) ), ( Connected Node v3, weight = w(v1,v3) ), ...]
                    Node v2: [( Connected Node v4, weight = w(v2,v4) ), ... ]
                    ...
                            :
                            :
                    Node vn: []
                }
        """
        self.nodes = list(digraph.keys())
        edges = {}
        for key, val in digraph.items():
            for v in val:
                '''
                d = {(key, v[0]): v[1],
                     (v[0], key): v[1]}
                '''
                d = {(key, v[0]): v[1]}
                edges.update(d)

        self.edges = edges
        neighbors = {}
        for key, val in digraph.items():
            temp_children = []
            for v in val:
                temp_children.append(v[0])
            d = {key: temp_children}
            neighbors.update(d)

        self.neighbors = neighbors

    def getEdges(self):
        return self.edges

    def getNodes(self):
        return self.nodes

    def updateEdgeCost(self, node1, node2, value):
        self.edges[(node1, node2)] = value

    def drawGraph(self, pos=lambda x: nx.planar_layout(x)):
        G = nx.DiGraph()
        G.add_nodes_from(self.nodes)
        G.add_edges_from([(key[0], key[1], {"travel_time": val}) for key, val in self.edges.items()])
        pos = pos(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, arrows=True)
        labels = nx.get_edge_attributes(G, "travel_time")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
