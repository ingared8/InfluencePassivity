__author__ = "ingared"

import networkx as nx
import os
import numpy as np
import re
from pylab import plot,show
from MyMulet2 import *
from ReadGraphFile import *
from IP import *

# The main script to run any Influence Passivity values of the network

if __name__ == '__main__':
    Ips=[]
    Inters=[]

    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/layer_1.txt"
    ip1 = InfluencePassivity(filename)
    ip1.run()
    Ips.append(ip1)
    print("going to street network")
    # Acceptance Ratio
    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/layer_2.txt"
    ip2 = InfluencePassivity(filename)
    ip2.run()
    Ips.append(ip2)
    #G2 = get_NY_StreetsGraph()
    #ip2.modifyGraph(G2)    
    #print ("check Street I:::", sum(ip2.I.values()))
    #print ("check Street P:::", sum(ip2.P.values()))
    
    
    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/layer_3.txt"
    ip3 = InfluencePassivity(filename)
    ip3.run()
    Ips.append(ip1)

    # inter layer
    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/interlayer_12.txt"
    inter1=InfluencePassivity(filename)
    inter1.run()
    Inters.append(inter1)
    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/interlayer_23.txt"
    inter2=InfluencePassivity(filename)
    inter2.run()
    Inters.append(inter2)

    MyMuLet2(layers=Ips, interLayers=Inters)
    #print ("chk sum:::",sum(ip.I.values()))
    #print ("chk sum2:::",sum(ip.P.values()))
