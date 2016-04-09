__author__ = "ingared"

import networkx as nx
import os
import numpy as np
import re
from pylab import plot,show
from MyMuLet import *
from ReadGraphFile import *
from IP import *

# The main script to run any Influence Passivity values of the network

if __name__ == '__main__':

    
    filename = "/Users/rashmijrao/Documents/IP-master/A1/Data/p2p-Gnutella08.txt"
    ip = InfluencePassivity(filename)
    Is=[]
    Ps=[]
    G1 = get_NY_UndergoundGraph()
    ip.modifyGraph(G1)
    ip.run()
    #print ("check:::",ip.I)
    #print ("check:::",ip.P)
    Is.append(ip.I)
    Ps.append(ip.P)
    print("going to street network")
    G2 = get_NY_StreetsGraph()
    ip.modifyGraph(G2)
    ip.run()
    Is.append(ip.I)
    Ps.append(ip.P)
    MuLet(layers = Is)
    print ("chk sum:::",sum(ip.I.values()))
    print ("chk sum2:::",sum(ip.P.values()))
