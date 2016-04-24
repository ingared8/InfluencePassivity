__author__ = "ingared"

import numpy as np
from IP import InfluencePassivity
from PageRank import PageRank
from MuLet import MuLet
import matplotlib.pyplot as plt
import networkx as nx

# The main script to run any Influence Passivity values of the network

if __name__ == '__main__':

    print "Main"

    filename = "/home/ingared/Documents/NS_IP/A1/Data/gnutella/p2p-Gnutella08.txt"
    filename2 = "/home/ingared/Documents/NS_IP/A1/Data/gnutella/Random3.txt"
    filename4 = "/home/ingared/Documents/NS_IP/A1/Data/gnutella/Random4.txt"

    ip2 = InfluencePassivity(filename2, weight=True)
    ip2.prepare()
    ip2.run()

    print ip2.I
    print ip2.P
    print np.sum(ip2.I.values())
    print np.sum(ip2.P.values())

    #filename1 = "/home/ingared/Documents/NS_IP/A1/Data/gnutella/Random.txt"
    #ip1 = InfluencePassivity(filename1, weight=True)
    #ip1.run()
    #print ip1.I
    #print ip1.P
    #print np.sum(ip1.I.values())
    #print np.sum(ip1.P.values())
    #m = MuLet()
    #m.update()

    print ip2.P
    print ip2.I

    pr = PageRank(filename2,directional=True)
    pr.pageRankAlgorithm(m=10)

    print pr.a
    print pr.h

    print "P",ip2.P
    print "I",ip2.I

    print ip2.I
    print ip2.P
    print np.sum(ip2.I.values())
    print np.sum(ip2.P.values())

    #nx.draw(pr.g)

    ip2 = InfluencePassivity(filename4, weight=True)
    ip2.ModifyWeightsToUnitScaleFromEdges()

    ip2.prepare()
    ip2.run()

    print ip2.I
    print ip2.P
    print np.sum(ip2.I.values())
    print np.sum(ip2.P.values())

    nx.draw_networkx(pr.g)
    plt.show()
