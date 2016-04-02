__author__ = "ingared"

import networkx as nx
import os
import numpy as np
import re
from pylab import plot,show

from ReadGraphFile import *
from IP import *

# The main script to run any Influence Passivity values of the network

if __name__ == '__main__':

    print "Main"
    filename = "/home/ingared/Documents/NS_IP/A1/Data/gnutella/p2p-Gnutella08.txt"
    ip = InfluencePassivity(filename)

    G = get_NY_UndergoundGraph()
    ip.modifyGraph(G)



    ip.run()

    print ip.I
    print ip.P
    print np.sum(ip.I.values())
    print np.sum(ip.P.values())
