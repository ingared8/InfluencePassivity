__author__ = "ingared"

import networkx as nx
import os
import numpy as np
import re
from pylab import plot,show
from MyMulet2 import *
from ReadGraphFile import *

# The main script to run any Influence Passivity values of the network

if __name__ == '__main__':
    Ips=[]
    Inters=[]

    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/layer1.txt"
    ip1 = InfluencePassivity(filename)
    ip1.ModifyWeightsToUnitScaleFromEdges()

    ip1.prepare()

    ip1.run()
    Ips.append(ip1)
    ip1.InfluencePassivityAlgorithm(mygraph=ip1.g, Avals=ip1.A, Rvals=ip1.R)
    with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Ilayer1.json', 'w') as outfile:
        json.dump(ip1.I, outfile)
    with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Player1.json', 'w') as outfile:
        json.dump(ip1.P, outfile)

    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/layer2.txt"
    ip2 = InfluencePassivity(filename)
    ip2.ModifyWeightsToUnitScaleFromEdges()

    ip2.prepare()

    ip2.run()

    Ips.append(ip2)
    ip2.InfluencePassivityAlgorithm(mygraph=ip2.g, Avals=ip2.A, Rvals=ip2.R)
    with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Ilayer2.json', 'w') as outfile:
        json.dump(ip2.I, outfile)
    with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Player2.json', 'w') as outfile:
        json.dump(ip2.P, outfile)

    #G2 = get_NY_StreetsGraph()
    #ip2.modifyGraph(G2)    

    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/layer3.txt"
    ip3 = InfluencePassivity(filename)
    ip3.ModifyWeightsToUnitScaleFromEdges()

    ip3.prepare()

    ip3.run()
    Ips.append(ip1)

    ip3.InfluencePassivityAlgorithm(mygraph=ip3.g, Avals=ip3.A, Rvals=ip3.R)
    with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Ilayer3.json', 'w') as outfile:
        json.dump(ip3.I, outfile)
    with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Player3.json', 'w') as outfile:
        json.dump(ip3.P, outfile)

    # inter layer
    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/interlayer1.txt"
    inter1=InfluencePassivity(filename)
    inter1.ModifyWeightsToUnitScaleFromEdges()

    inter1.prepare()

    inter1.run()
    Inters.append(inter1)

    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/interlayer2.txt"
    inter2=InfluencePassivity(filename)
    inter2.ModifyWeightsToUnitScaleFromEdges()

    inter2.prepare()
    inter2.run()
    Inters.append(inter2)

    filename = "/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/interlayer3.txt"
    inter3 = InfluencePassivity(filename)
    inter3.ModifyWeightsToUnitScaleFromEdges()

    inter3.prepare()
    inter3.run()
    Inters.append(inter3)

    MyMuLet2(layers=Ips, interLayers=Inters)
    #print ("chk sum:::",sum(ip.I.values()))
    #print ("chk sum2:::",sum(ip.P.values()))
