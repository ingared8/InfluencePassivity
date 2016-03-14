__author__ = "ingared"

import networkx as nx
import os
import numpy as np
import re

from ReadGraphFile import *

# The main script to run any Influence Passivity values of the network

class InfluencePassivityValues():

    # -- Graph
    g = None

    # Acceptance Ratio
    A = {}
    NormA = {}

    # Rejectance Ratio
    R = {}
    NormR = {}

    # Influeence Scores
    I = {}
    NormI = {}

    # Passivity Scores
    P = {}
    NormP = {}

    def __init__(self,filename, directional= True, weight = False):

        """

        :param filename: filename in which data is present
        :param directional: Boolean -- Whether Graph is directed (True) or not (False)
        :param weight: Boolean -- Weights for edges are present (True) or not present ( False)
        :return: None as its a constructor
        """

        # Create Graph from file


        self.g =  readGraphfromFile(filename=filename, directional= directional, weight=weight)
        self.weight = weight


    def detCumulativeAcceptanceValues(self):
        """
        Acceptance rate defined as

                      w(i,j)
        u(i,j) =  ---------------
                    Sum(w(k,j))

        Cumulative Acceptance is defined as Sum(w(k,j))

        for all i E (V, nodes), (i,j) E (E, Edges), (k,j) E (E, Edges)

        :return: None
        """
        if(not(self.weight)):
            for nodej in self.g.nodes():
                self.NormA[nodej] = len(self.g.in_edges(nodej))
        else:
            for nodej in self.g.nodes():
                WeightedSum = 0.0
                for edge in self.g.in_edges(nodej):
                    weight = self.g.get_edge_data(edge[0,edge[1]])
                    WeightedSum += weight
                self.NormA[nodej] = WeightedSum


    def detAcceptanceRateValues(self):
        """
        Acceptance rate defined as

                      w(i,j)
        u(i,j) =  ---------------
                    Sum(w(k,j))

        for all i E (V, nodes), (i,j) E (E, Edges), (k,j) E (E, Edges)
        :return:
        """
        if(not(self.weight)):
            for nodej in self.g.nodes():
                WeightedSum = len(self.g.in_edges(nodej))
                for edge in self.g.in_edges(nodej):
                    self.A[edge[0] + "-"+edge[1]] = (1.0/self.NormA[nodej])
        else:
            for nodej in self.g.nodes():
                for edge in self.g.in_edges(nodej):
                    self.A[edge[0] + "-"+edge[1]] = (self.g.get_edge_data(edge[0],edge[1]) + 0.0)/self.NormA[nodej]


    def detCumulativeRejectanceValues(self):
        """
        Rejectance rate is defined as

                     1- w(i,j)
        u(i,j) =  ---------------
                    Sum(1 - w(k,j))

        Cumulative Rejectance is defined as Sum(1 - w(k,j))

        for all i E (V, nodes), (i,j) E (E, Edges), (k,j) E (E, Edges)

        :return: None
        """
        if(not(self.weight)):
            for nodej in self.g.nodes():
                self.NormR[nodej] = len(self.g.out_edges(nodej))
        else:
            for nodej in self.g.nodes():
                WeightedSum = 0.0
                for edge in self.g.out_edges(nodej):
                    weight = self.g.get_edge_data(edge[0,edge[1]])
                    WeightedSum += (1 - weight)
                self.NormR[nodej] = WeightedSum

    def detRejectanceRateValues(self):
        """
        Acceptance rate defined as

                    1 - w(i,j)
        u(i,j) =  ---------------
                   Sum(1 - w(k,j))

        for all i E (V, nodes), (i,j) E (E, Edges), (k,j) E (E, Edges)
        :return:
        """
        if(not(self.weight)):
            for nodej in self.g.nodes():
                for edge in self.g.out_edges(nodej):
                    self.R[edge[0] + "-"+edge[1]] = (1.0/self.NormR[nodej])
        else:
            for nodej in self.g.nodes():
                for edge in self.g.out_edges(nodej):
                    self.R[edge[0] + "-"+edge[1]] = (1.0 - self.g.get_edge_data(edge[0],edge[1]) )/self.NormR[nodej]

    def detInfluenceValues(self,P):

        """
        :return:
        """
        I = {}
        for node in self.g.nodes():
            weight = 0.0
            for edge in self.g.out_edges(node):
                weight += self.A[edge[0]+"-"+edge[1]]*P[node]
            I[node] = weight
        return I

    def detPassivityValues(self,I):
        """

        :return:
        """
        P = {}
        for node in self.g.nodes():
            weight = 0.0
            for edge in self.g.in_edges(node):
                weight += self.R[edge[0]+"-"+edge[1]]*I[node]
            P[node] = weight
        return P


    def InfluencePassivityAlgorithm(self, m= 100):

        """
        :return:
        """

        for node in self.g.nodes():
            self.P[node] = 1
            self.I[node] = 1

        iter =1
        error = 100
        errorLimit = 0.01
        Ierror = 0.0
        Perror = 0.0
        while ( (iter < m) & (error < errorLimit)):
            I = self.detInfluenceValues(self.P)
            P = self.detPassivityValues(self.I)
            sumI = np.sum(I.values()) + 0.0
            sumP = np.sum(P.values()) + 0.0
            for node in self.g.nodes():
                ivalue = I[node]/(sumI)
                pvalue = P[node]/(sumP)
                Ierror += abs(ivalue - self.I[node])
                Perror += abs(pvalue - self.P[node])
                self.I[node] = I[node]/(sumI)
                self.P[node] = P[node]/(sumP)
                error = (Ierror/sumI) + (Perror/sumP)
            iter += 1