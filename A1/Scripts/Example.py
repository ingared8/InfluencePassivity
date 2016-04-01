#!/usr/local/python-2.7.10/bin/python

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_nodes_from([1,2,3,4,5,6,7])
G.add_edges_from([(1,2),(1,3),(3,4),(2,5),(4,5),(5,6)])

G.add_nodes_from(['a','b'])
G.add_edges_from(([('a',1),('b','a')]))

print nx.shortest_path(G,1,6)
print nx.number_connected_components(G)

nx.draw_networkx(G)
plt.show()
