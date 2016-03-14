# cuts.py - functions for computing and evaluating cuts
#
# Copyright 2011 Ben Edwards <bedwards@cs.unm.edu>.
# Copyright 2011 Aric Hagberg <hagberg@lanl.gov>.
# Copyright 2015 NetworkX developers.
#
# This file is part of NetworkX.
#
# NetworkX is distributed under a BSD license; see LICENSE.txt for more
# information.
"""Functions for finding and evaluating cuts in a graph.

"""
from __future__ import division

from itertools import chain

import networkx as nx

__all__ = ['boundary_expansion', 'conductance', 'cut_size', 'edge_expansion',
           'mixing_expansion', 'node_expansion', 'normalized_cut_size',
           'volume']

global edges1

# TODO STILL NEED TO UPDATE ALL THE DOCUMENTATION!

def cut_size(G, S, T=None, weight=None):
     """Returns the size of the cut between two sets of nodes.
     A *cut* is a partition of the nodes of a graph into two sets.
     The *cut size* is the sum of the weights of the edges "between" the two sets of nodes.
     Parameters ---------- G :
        NetworkX graph S : sequence A sequence of nodes in ``G``.
        T : sequence A sequence of nodes in ``G``.
        If not specified, this is taken to be the set complement of ``S``.
        weight : object Edge attribute key to use as weight.
        If not specified, edges have weight one. Returns ------- number
        Total weight of all edges from nodes in set ``S`` to nodes in set ``T`` (and, in the case of directed graphs, all edges from nodes in ``T`` to nodes in ``S``).

     Examples -------- In the graph with two cliques joined by a single edges, the natural bipartition of the graph into two blocks,
     one for each clique, yields a cut of weight one:: >>>

     G = nx.barbell_graph(3, 0) >>>
     S = {0, 1, 2}
     T = {3, 4, 5}
     nx.cut_size(G, S, T) 1
     Each parallel edge in a multigraph is counted when determining the cut size::
    G = nx.MultiGraph(['ab', 'ab'])
    S = {'a'}
    T = {'b'}
    nx.cut_size(G, S, T)
    Notes ----- In a multigraph, the cut size is the total weight of edges including multiplicity.

    """
     edges = nx.edge_boundary(G, S, T,)
     if G.is_directed():
         edges = chain(edges, nx.edge_boundary(G, T, S))
     #return sum(weight for u, v, weight in edges)
     #print len(edges)
     return len(edges)

def volume(G, S, weight=None):

     """
     Returns the volume of a set of nodes.
     The *volume* of a set *S* is the sum of the (out-)degrees of nodes in *S* (taking into account parallel edges in multigraphs).
     [1] Parameters ---------- G : NetworkX graph S :

     sequence A sequence of nodes in ``G``. weight : object Edge attribute key to use as weight.

     If not specified, edges have weight one. Returns ------- number
     The volume of the set of nodes represented by ``S`` in the graph ``G``.
     See also -------- conductance cut_size edge_expansion edge_boundary normalized_cut_size

     References ---------- .. [1] David Gleich.
     *Hierarchical Directed Spectral Graph Partitioning*.
     <https://www.cs.purdue.edu/homes/dgleich/publications/Gleich%202005%20-%20hierarchical%20directed%20spectral.pdf>
     """

     degree = G.out_degree if G.is_directed() else G.degree
     return sum(degree(S, weight=weight).values())

def normalized_cut_size(G, S, T=None, weight=None):

     if T is None:
         T = set(G) - set(S)
     num_cut_edges = cut_size(G, S, T=T, weight=weight)
     volume_S = volume(G, S, weight=weight)
     volume_T = volume(G, T, weight=weight)
     return num_cut_edges * ((1.0 / volume_S) + (1.0 / volume_T))


def conductance(G, S, T=None, weight=None):

    if T is None:
        T = set(G) - set(S)

    num_cut_edges = cut_size(G, S, T, weight=weight)
    volume_S = volume(G, S, weight=weight)
    volume_T = volume(G, T, weight=weight)
    return num_cut_edges / min(volume_S, volume_T)


def get_n_cut_and_conductance(G,S,T=None, weight=None):
    if T is None:
        T = set(G) - set(S)
    num_cut_edges = cut_size(G, S, T, weight=weight)
    volume_S = volume(G, S, weight=weight)
    volume_T = volume(G, T, weight=weight)
    #print "Volume" , num_cut_edges, volume_S, volume_T
    return num_cut_edges*((1.0/volume_S) + (1.0/volume_T)) ,num_cut_edges / min(volume_S, volume_T)


def edge_expansion(G, S, T=None, weight=None):

     if T is None:
         T = set(G) - set(S)
     num_cut_edges = cut_size(G, S, T=T, weight=weight)
     return num_cut_edges / min(len(S), len(T))


def mixing_expansion(G, S, T=None, weight=None):
     num_cut_edges = cut_size(G, S, T=T, weight=weight)
     num_total_edges = G.number_of_edges()
     return num_cut_edges / (2 * num_total_edges)


# TODO What is the generalization to two arguments, S and T? Does the
# denominator become `min(len(S), len(T))`?

def node_expansion(G, S):
    neighborhood = set(chain.from_iterable(G.neighbors(v) for v in S))
    return len(neighborhood) / len(S)


# TODO What is the generalization to two arguments, S and T? Does the
# denominator become `min(len(S), len(T))`?

def boundary_expansion(G, S):
    return len(nx.node_boundary(G, S)) / len(S)
