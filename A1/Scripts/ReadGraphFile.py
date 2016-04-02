__author__ = "ingared"

import networkx as nx
import os
import numpy as np
import re
import dbf
from dbfread import DBF

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
                g.add_weighted_edges_from([(vals[0],vals[1], weight_value)], color = 'red')
            linecount += 1
            if ( linecount%100 == 0):
                print "Reading line no: ",linecount
    f.close()
    print "File Reading Completed"
    return g


def get_NY_StreetsGraph():

    dir  = "/home/ingared/Documents/NS_IP/UndergroundData"
    ny_streets = "NY_STREETS.dbf"

    g = nx.DiGraph()

    count = 0
    test1 = DBF(os.path.join(dir,ny_streets))
    print " Started reading NY Street data\n"

    for record in test1:

        edge_id = record['edge_ID']
        fn_id = record['FN_ID']
        tn_id = record['TN_ID']
        length = record['length']

        #print fn_id,tn_id,length, edge_id

        if ( not g.has_node(fn_id)):
            g.add_node(fn_id)
        if (not g.has_node(tn_id)):
            g.add_node(fn_id)
        g.add_weighted_edges_from([(fn_id,tn_id,length)],edge_id=edge_id)
        g.add_weighted_edges_from([(tn_id,fn_id,length)],edge_id=edge_id)

        count += 1
        if (count%1000 == 0):
            print "No of edges read :", count

    print '\n'
    print " Total Edges in Streets  : " , count
    print '\n'

    return g


def get_NY_UndergoundGraph():

    dir  = "/home/ingared/Documents/NS_IP/UndergroundData"
    ny_streets = "NY_UNDERGROUND.dbf"

    g = nx.DiGraph()

    count = 0
    test1 = DBF(os.path.join(dir,ny_streets))
    print " Started reading NY Underground data\n"

    for record in test1:
        edge_id = str(record['edge_ID'])
        fn_id = str(record['FN_ID'])
        tn_id = str(record['TN_ID'])
        length = record['length']
        fn_x = record['FN_x']
        fn_y = record['FN_y']
        tn_x = record['TN_x']
        tn_y = record["TN_y"]
        name = record['name']
        type = record['type']

        #print fn_id,tn_id,length, edge_id
        if ( not g.has_node(fn_id)):
            g.add_node(fn_id)
        if (not g.has_node(tn_id)):
            g.add_node(fn_id)

        g.add_weighted_edges_from([(fn_id,tn_id,length)],edge_id=edge_id,fn_x=fn_x,fn_y=fn_y,
                                  tn_x = tn_x,tn_y = tn_y,name = name,type= type)

        g.add_weighted_edges_from([(tn_id,fn_id,length)],edge_id=edge_id,tn_y=fn_y,tn_x=fn_x,
                                  fn_x = tn_x,fn_y = tn_y,name = name,type= type)
        count += 1
        if (count%1000 == 0):
            print record
            print "No of edges read :", count

    print '\n'
    print " Total Edges in Streets  : " , count
    print '\n'
    return g

def convertGraphWeightsToFractions(g):

    """
    This is to convert any graph with liberal weights to a fractional value
    which refers to the acceptance levels between them.
    :return:

    """

    total_weight = 0.0
    for node in g.nodes():
        for edge in g.in_edges(node):
            total_weight += g.get_edge_data()

def getTotalWeight(g):

    totalWeight = 0.0
    for edge in g.edges_iter(data='weight'):
        totalWeight += edge[-1]

#g1 = get_NY_StreetsGraph()
#g2 = get_NY_UndergoundGraph()
#print " Street data from 1 to 2"
#g1.get_edge_data('1','2')
#print " Underground metro from 1 to 2"
#print g2.get_edge_data('1','2')