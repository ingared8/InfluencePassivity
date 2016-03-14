__author__ = "ingared"

import networkx as nx
import os
import numpy as np
import re

# Common functions
def splitLine (line):
    return re.sub("[^\w]", " ",  line).split()

def readGraphfromFile(filename, delimiter = "#", weight = False, directional = True):
    """
    Generates a graph from data present in a file
    :param filename: String  --> Name of the file
    :param delimiter: String Char --> Delimiter to ignore the sentences
    :param weight: Boolean  --> Weighs of the edges are present in graph
    :param direction Boolean --> Graph is directed
    :return: nx.DiGraph()/ nx.Graph()
    """

    if (not(directional)):
        g = nx.Graph()
    else:
        g = nx.DiGraph()
    f = open(filename, 'r')
    linecount = 0
    print " File Reading Started"
    for line in f:
            if (line[0] == delimiter):
                pass
            else:
                vals = splitLine(line)
                # Check if node is present in graph
                if ( not g.has_node(vals[0])):
                    g.add_node(vals[0])
                if ( not g.has_node(vals[1])):
                    g.add_node(vals[1])
                if ((len(vals) > 2) & weight):
                    weight_value = vals[2]
                else:
                    weight_value = 1
                g.add_weighted_edges_from([(vals[0],vals[1],weight_value)], color = 'red')
            linecount += 1
            if ( linecount%100 == 0):
                print "Reading line no: ",linecount
    f.close()
    print "File Reading Completed"
    return g

