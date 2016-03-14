import networkx as nx
import community
import matplotlib as plt

"""
G = nx.random_graphs.powerlaw_cluster_graph(300, 1, .4)

part = community.best_partition(G)
values = [part.get(node) for node in G.nodes()]

nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
"""
degree_sum_dict = {}
community_dict = {0:{0,1},1:{2,3}}
data_graph = nx.complete_graph(4)
for key in community_dict:
    list = community_dict[key]
    sum = 0;
    for i in list:
        sum += data_graph.degree(i);
    degree_sum_dict[key] = sum

print degree_sum_dict