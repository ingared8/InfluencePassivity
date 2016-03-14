import networkx as nx
import os
import numpy as np
import re

# Commonly used commands are used with short names

# Initialize a graph
g = nx.DiGraph()

# Common functionalities
def splitLine (line):
    return re.sub("[^\w]", " ",  line).split()

# Read the file
print "Started reading file"
f = open('A1/Data/gnutella/p2p-Gnutella08.txt', 'r')
linecount = 0
user = None
nomin = None
for line in f:
        c = line[0]

        if (c == '#'):
            pass
        else:
            vals = splitLine(line)

            if ( not g.has_node(vals[0])):
                g.add_node(vals[0])
            if ( not g.has_node(vals[1])):
                g.add_node(vals[1])

            g.add_weighted_edges_from([(vals[0],vals[1],1)], color = 'red')

        linecount += 1
        if ( linecount%100 == 0):
            print "Reading line no: ",linecount

f.close()
print " File Reading Completed"


print "Calculating Degree Centrality"
# Degree Centrality ( in- deggree and out-degree )
nodes = np.asarray(g.nodes())

in_DegCor = {}
out_DegCor = {}
normIn_DegCor = {}
normOut_DegCor = {}
length = len(nodes)

for node in (nodes):
    in_DegCor[node] = g.in_degree(node)
    out_DegCor[node] = g.out_degree(node)
    normIn_DegCor[node] = (in_DegCor[node])/(0.0 + length-1)
    normOut_DegCor[node] = (out_DegCor[node])/(0.0 + length-1)


# Save the values
np.savez('A1/output/gnutella/degreeCentrality', in_DegCor,out_DegCor,normIn_DegCor,normOut_DegCor)

print "Calculating Closeness Centrality"
# Closeness Centrality
closenessCentrality = nx.closeness_centrality(g)
np.savez('A1/output/gnutella/closenessCentrality', closenessCentrality)


print "Calculating Betweenness Centrality"

# Betweenness Centrality
betweennessCentrality= nx.betweenness_centrality(g)
np.savez('A1/output/gnutella/betweennessCentrality', betweennessCentrality)


print "Calculating Harmonic Centrality"
# Harmonic Centrality
harmonicCentrality = nx.harmonic_centrality(g)
np.savez('A1/output/gnutella/harmonicCentrality', harmonicCentrality)

"""
def getDiameterAndRadius(inEccentricity):
    diameter = max(inEccentricity.values())
    radius = min(inEccentricity.values())
    return diameter,radius

# Eccentricity and radius
inEccentricity = {}
outEccentricity = {}

for node in nodes:
    inEccentricity[node] = -1
    outEccentricity[node] = -1

for key,val in shortestPathDict.iteritems():
    for key1, value1 in val:
        length = len(value1)-1
        inEccentricity[key] = max(inEccentricity[key],length)
        outEccentricity[key1] = max(outEccentricity[key1],length)


np.savez('A1/output/gnutella/eccentricity', inEccentricity, outEccentricity)

print "Diameter and Radius for In Eccentricity is " , getDiameterAndRadius(inEccentricity)
print "Diameter and Radius for Out Eccentricity is " , getDiameterAndRadius(outEccentricity)
"""

print "Calculating Clustering Cofficient"
# Clustering Cofficient
#ug = g.to_undirected()
#clusteringCofficient = nx.clustering(ug, nodes, weight=None)

ug1 = g.to_undirected(reciprocal=True)
clusteringCofficientWithReciprocal = nx.clustering(ug1, nodes, weight=None)

# Network Clustering Cofficient
networkCltedusteringCofficient = np.mean(clusteringCofficient.values())
networkCltedusteringCofficientReciprocal = np.mean(clusteringCofficientWithReciprocal.values())

print "networkClusteringCofficent is ", networkCltedusteringCofficient, networkCltedusteringCofficientReciprocal
np.savez('A1/output/gnutella/clusteringCofficient', clusteringCofficient,clusteringCofficientWithReciprocal)

# PageRank Centrality
print "Calculating PageRank Centrality"
pageRank = nx.pagerank(g,alpha=0.85,personalization=None,weight='weight', dangling=None)
np.savez('A1/output/gnutella/pageRank', pageRank)

print "Calculating Eigen Vector Centrality"
# Eigen Vector
eigenVector = nx.eigenvector_centrality(g,max_iter=40,tol=1.0e-4,nstart=None,weight='weight')
np.savez('A1/output/gnutella/eigenVector', eigenVector)
