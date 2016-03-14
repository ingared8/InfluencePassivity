import networkx as nx
import os
import numpy as np
import re

# Commonly used commands are used with short names

# Initialize a graph
g = nx.Graph()

# Common functionalities
def splitLine (line):
    return re.sub("[^\w]", " ",  line).split()

# Read the file
print "Started reading file"
f = open('A1/Data/facebook/facebook_combined.txt', 'r')
linecount = 0

for line in f:
        vals = splitLine(line)
        g.add_edges_from([(vals[0],vals[1])], color='blue')

        linecount += 1
        if ( linecount%100 == 0):
            print "Reading line no: ", linecount

f.close()
print "File Reading Completed"

print "Calculating Degree Centrality"
# Degree Centrality ( in- deggree and out-degree )
nodes = np.asarray(g.nodes())

in_DegCor = {}
normIn_DegCor = {}
length = len(nodes)

for node in (nodes):
    in_DegCor[node] = g.degree(node)
    normIn_DegCor[node] = (in_DegCor[node])/(0.0 + length-1)

# Save the values
np.savez('A1/output/facebook/degreeCentrality', in_DegCor,normIn_DegCor)

print "Calculating Closeness Centrality"
# Closeness Centrality
closenessCentrality = nx.closeness_centrality(g)
np.savez('A1/output/facebook/closenessCentrality', closenessCentrality)


print "Calculating Betweenness Centrality"
# Betweenness Centrality
betweennessCentrality= nx.betweenness_centrality(g)
np.savez('A1/output/facebook/betweennessCentrality', betweennessCentrality)


print "Calculating Harmonic Centrality"
# Harmonic Centrality
harmonicCentrality = nx.harmonic_centrality(g)
np.savez('A1/output/facebook/harmonicCentrality', harmonicCentrality)

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


np.savez('A1/output/facebook/eccentricity', inEccentricity, outEccentricity)

print "Diameter and Radius for In Eccentricity is " , getDiameterAndRadius(inEccentricity)
print "Diameter and Radius for Out Eccentricity is " , getDiameterAndRadius(outEccentricity)
"""

print "Calculating Clustering Cofficient"
# Clustering Cofficient
clusteringCofficient = nx.clustering(g, nodes, weight=None)

# Network Clustering Cofficient
networkCltedusteringCofficient = np.mean(clusteringCofficient.values())

print "networkClusteringCofficent is ", networkCltedusteringCofficient
np.savez('A1/output/facebook/clusteringCofficient', clusteringCofficient)

# PageRank Centrality
print "Calculating PageRank Centrality"
pageRank = nx.pagerank(g,alpha=0.85,personalization=None,weight='weight', dangling=None)
np.savez('A1/output/facebook/pageRank', pageRank)

print "Calculating Eigen Vector Centrality"
# Eigen Vector
eigenVector = nx.eigenvector_centrality(g,max_iter=40,tol=1.0e-4,nstart=None,weight='weight')
np.savez('A1/output/facebook/eigenVector', eigenVector)
