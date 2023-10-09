"""
CSE551
Assignment 3
Author: Rohan Rele
"""

import networkx as nx
from heapq import heapify, heappush, heappop
from cse551a3_graph import Graph, cost_f, f_e


def random_Dijkstra(graph, source, target):
    S = []  # priority queue of unexplored nodes
    heapify(S)  # we turn this into a binomial min heap for fast access
    heappush(S, (source, 0))  # add the source node and its distance from the source (0) to heap
    min_running_dist = {node: 1000000 for node in
                        graph.getNodes()}  # dictionary data structure for 'pi' values, shortest running path to node--key
    min_running_dist[source] = 0  # π(source) = 0

    incident_nodes = graph.neighbors  # get neighboring node list for each edge in dict format

    while S:  # while heap not empty i.e., there are unexplored nodes
        u, d_u = heappop(S)  # remove the root node
        for v in incident_nodes[u]:  # find all of its neighbors
            minimum_travel_time = graph.getEdges()[(u, v)]  # find the travel time without noise
            noisy_travel_time = f_e(
                minimum_travel_time)  # make the "API Call", find the noisy travel time between nodes u and v
            # noisy_travel_time = minimum_travel_time  # debugging line
            graph.updateEdgeCost(u, v, noisy_travel_time)  # update graph

        for v in incident_nodes[u]:  # now that we have our new 'noisy' options, we perform the actual dijkstra's loop
            new_time = graph.getEdges()[(u, v)]  # convenience travel time variable
            if min_running_dist[v] > min_running_dist[u] + new_time:  # if π(v) > π(u) + d(v)
                min_running_dist[v] = min_running_dist[u] + new_time  # set π(v) = π(u) + d(v)
                heappush(S, (v, min_running_dist[v]))  # add v to the heap and set its new minimal distance

    # algorithm will terminate upon the target node being removed from the heap

    return min_running_dist[target], graph


'''
simple_G = Graph({
    1: [(2, 15), (3, 12)],
    2: [(3, 4)],
    3: []
})
'''

given_G = Graph({
    1: [(2, 9), (6, 14), (7, 15)],
    2: [(3, 23)],
    3: [(8, 19), (5, 2)],
    4: [(3, 6), (8, 6)],
    5: [(4, 11), (8, 16)],
    6: [(3, 18), (5, 30), (7, 5)],
    7: [(5, 20), (8, 44)],
    8: []
})

'''

working_G = Graph({

    "A": [("B", 2), ("C", 6)],
    "B": [("D", 5)],
    "C": [("D", 8)],
    "D": [("F", 15), ("E", 10)],
    "E": [("F", 6), ("G", 2)],
    "F": [("G", 6)],
    "G": []
})
'''

'''
pos = lambda x: nx.shell_layout(x)
g = Graph(working_G)
print(g.getEdges())
print(g.getNodes())
g.updateEdgeCost("A", "C", 90)
print(g.getEdges())
print(g.getNodes())
g.drawGraph(pos)
'''
src = 1  # source
trgt = 8  # target
path_len, grph = random_Dijkstra(given_G, src, trgt)
print("Shortest Path from Nodes", src, "to", trgt, "is:", path_len)
grph.drawGraph(lambda x: nx.kamada_kawai_layout(x))
