__author__ = 'rakshith'

import os
import re
import networkx as nx
import operator
import string
from cutLib import get_n_cut_and_conductance
from pylab import plot,show
import numpy as np

def graph_from_metisfile(input_file):
    #graph = nx.read_adjlist('./'+input_file,comments='5241 14484',create_using=nx.Graph(), nodetype=int)
    file = open('./'+input_file)
    lines = file.readlines()
    line_count = 0
    graph = nx.Graph()
    for line in lines:
        if line_count == 0:
            line_count += 1
            continue
        for i in line.split():
            graph.add_edge(line_count,int(i),weight= 1)
        line_count += 1
    return graph

def community_list_from_file(community_file):
    file = open(community_file)
    lines = file.readlines()
    line_count = 0
    community = {}
    for line in lines:
        if int(line.split()[0]) not in community.keys():
            list = []
            list.append(line_count)
            community[int(line.split()[0])] = list
        else:
            community[int(line.split()[0])].append(line_count)
        #if line_count < 5:
            #print line_count," ",line.split()[0]
        line_count += 1
    return community

def community_map_from_file(community_file):
    file = open(community_file)
    lines = file.readlines()
    line_count = 1
    community = {}
    for line in lines:
        community[line_count] = int(line.split()[0])
        line_count += 1
    return community

def number_of_clusters(community_map_dict):
    return max(community_map_dict.iteritems(), key=operator.itemgetter(1))[1]

def sum_of_degree_of_nodes_in_community(data_graph, community_list_dict, k):
    list = community_list_dict[k]
    sum = 0;
    degree = data_graph.degree()
    for i in list:
        sum += degree[i]
    return sum

def delta(i,j,community_map_dict):
    #return 1 if two different nodes belong to the same community.
    if community_map_dict[i] == community_map_dict[j]:
        return 1
    else:
        return 0

def compute_modularity(data_graph,community_map_dict,file_type):
    if file_type == "":
        n = data_graph.number_of_nodes()
        m = data_graph.number_of_edges()
        #p = 2*m/(n(n-1)) -- For null model.
        nc = number_of_clusters(community_map_dict)
        print "number of nodes  : ",n
        print "number of edges : ",m
        print "number of clusters : ",nc
        Q = 0.0
        degree = data_graph.degree()
        for i in range(1,n):
            ki = degree[i]
            for j in range(1,n):
                kj = degree[j]
                Pij = ki*kj/(2*m)
                if data_graph.has_edge(i,j):
                    Aij = 1
                else:
                    Aij = 0
                d = delta(i,j,community_map_dict)
                Q += (Aij - Pij)*d
        Q = (Q)/(2*m)
        print "Modularity = ",Q
        return Q

"""
def compute_conductance(data_graph,community_dict,file_type):
    if file_type == "":
        n = data_graph.number_of_nodes()
        m = data_graph.number_of_edges()
        Conductance
        c = cutsize(community_dict,data_graph,i)
        kc =  sum_of_degree_of_nodes_in_community(community_dict,data_graph,i)
        kgc = m - c - kc

"""
def cutsize(data_graph,community_list_dict,community_map_dict,i):
    list = community_list_dict[i]
    adj_list = data_graph.adjacency_list()
    cutsize_value = 0
    for i in list:
        print i,"->",adj_list[i]
        for j in adj_list[i]:
            if(delta(i,j,community_map_dict)==0):
                cutsize_value += 1


def conductanceAndNcut(G,community_list_dict):

    conductance = {}
    nCut = {}
    for key,value in community_list_dict.iteritems():
        nCut[key],conductance[key] = get_n_cut_and_conductance(G,value)
    return conductance,nCut

def savefigure( dict, name, type ):
    try:
        import matplotlib.pyplot as plt
        my_dpi = 96
        plt.figure(1,figsize=(200/my_dpi, 200/my_dpi), dpi=my_dpi)
        values = dict.values()/np.mean(dict.values())
        types = type.split(".")
        #print types
        savename = types[0]+"."+types[2]
        #print savename
        plt.plot( values,'b*')
        plt.title(savename)
        filename = (savename + "." + name + ".jpg")
        plt.savefig(filename)
        plt.close()
    except:
        print "Matplotlib is not available"

    try:
        values = dict.values()
        print type, name, filename
        print " Mean  : " , np.mean(values)
        print " std/Mean   : " , np.std(values)/np.mean(values)
    except:
        pass

#community_dict = dict_from_file('ca-GrQc.metis.c100.i2.0.b0.6',"nothing")
#data_graph = graph_from_file('../ca-GrQc.txt')
#data_graph = graph_from_metisfile('../ca-GrQc.metis')
#print data_graph.number_of_nodes()
#print data_graph.number_of_edges()
#print data_graph.degree()
#print sum_of_degrees(community_dict,data_graph)
#print dict_from_file2('ca-GrQc.metis.c100.iv
graph_file_list = ['ca-GrQc.metis','facebook_combined.metis','p2p-Gnutella08.metis','wiki-Vote.metis']
community_file_List = ['c100.i2.0.b0.6','c500.i2.0.b0.6','c1000.i2.0.b0.6']
for graph_file in graph_file_list:
    for comfile in community_file_List:
        community_file = graph_file + "." + comfile
        data_graph = graph_from_metisfile(graph_file)

        community_map_dict = community_map_from_file(community_file)
        community_list_dict = community_list_from_file(community_file)

        #compute_modularity(data_graph,community_dict2,"")
        #print community_list_dict[2]
        #print sum_of_degree_of_nodes_in_community(data_graph, community_list_dict,2)
        #print cutsize(data_graph, community_list_dict,community_map_dict,4)
        cond,nCut = conductanceAndNcut(data_graph,community_list_dict)
        savefigure(nCut,"nCut",community_file)
        #savefigure(cond,"Conductance",community_file)