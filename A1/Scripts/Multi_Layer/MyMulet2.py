__author__ = "ingared"

import networkx as nx
import json
from MyIP import *
from PageRank import *
class MyMuLet2():

    """"
    A multi layer network.
    The same network showing different behaviours can be best represented using a multi layer network.
    """

    layers = []
    interLayers=[]
    weights = None

    # Acceptance Ratio
    A = {}
    NormA = {}

    # Delta Refers to inter layer connections
    # Star refers to intra layer connections

    A_delta = {}
    NormA_delta = {}

    A_star = {}
    NormA_star = {}

    # Rejectance Ratio
    R = {}
    NormR = {}

    R_delta = {}
    NormR_delta = {}

    R_star = {}
    NormR_star = {}

    # Influeence Scores
    I = {}

    # Passivity Scores
    P = {}

    #Graph
    g = None


    def __init__(self,layers = None, interLayers = None, weights = None):

        """
        Construct a Mulet with a list of individual layers.
        weights represent the inter layer edges between different layers.
        :return: None
        """
        if layers is not None:
             self.layers = layers
        if weights is not None:
            self.weights = weights
        if interLayers is not None:
            self.interLayers=interLayers
        self.getGenericGraphfromLayers()
        self.detCumulativeIntraLayerAcceptance()
        self.updateCumulativeAcceptance()

        self.detCumulativeInterLayerAcceptance()
        self.detCumulativeIntraLayerRejectance()
        self.updateCumulativeRejectance()

        self.detCumulativeInterLayerRejectance()
        finIp=InfluencePassivity(filename=None)

        finIp.InfluencePassivityAlgorithm(mygraph=self.g,Avals=self.A_delta,Rvals=self.R_delta)
        with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Influences.json', 'w') as outfile:
            json.dump(finIp.I, outfile)
        with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Passivities.json', 'w') as outfile:
            json.dump(finIp.P, outfile)

        print('Sum I:::',str(max((finIp.I.values()))))
        print('Sum P:::',str(max((finIp.P.values()))))

        pr = PageRank( directional=True)
        pr.modifyGraph(self.g)
        pr.pageRankAlgorithm(m=10)

        with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Authority.json', 'w') as outfile:
            json.dump(pr.a, outfile)
        with open('/Users/rashmijrao/Documents/IP-master/A1/Scripts2/NS_Final/Hub.json', 'w') as outfile:
            json.dump(pr.h, outfile)

        print ('pagerank a:::',max(pr.a.values()))
        print ('pagerank h:::',max(pr.h.values()))

    def getGenericGraphfromLayers(self):

        """
        Generate a graph which covers every node of the multi layers
        :return:
        """
        self.g = nx.MultiDiGraph()

        for layer in self.layers:
            for node in layer.g.nodes():
                if not (self.g.has_node(node)):
                    self.g.add_node(node)
                else:
                    pass


        # Defaulting all values of A and R to floating zeroes
        for layer in self.layers:
            for edge in layer.g.edges_iter():
                key = edge[0] + "-" + edge[1]
                self.A_delta[key] = 0.0
                self.A_star[key]= 0.0
                self.R_delta[key] = 0.0
                self.R_star[key]  = 0.0
                self.A[key] = 0.0
                self.R[key] = 0.0
                self.NormA[edge[0]]= 0.0
                self.NormR[edge[0]] = 0.0
                self.NormA[edge[1]] = 0.0
                self.NormR[edge[1]] = 0.0

        for layer in self.interLayers:
            for edge in layer.g.edges_iter():
                key = edge[0] + "-" + edge[1]
                self.A_delta[key] = 0.0
                self.A_star[key] = 0.0
                self.R_delta[key] = 0.0
                self.R_star[key] = 0.0
                self.A[key] = 0.0
                self.R[key] = 0.0
                self.NormA[edge[0]] = 0.0
                self.NormR[edge[0]] = 0.0
                self.NormA[edge[1]] = 0.0
                self.NormR[edge[1]] = 0.0

    def updateCumulativeAcceptance(self):

        """
        Update the total acceptance from i
        as A is column stochastic matrix
        :return:
        """
        for layer in self.layers:
            for key,value in layer.NormA.items():
                if key in self.NormA:
                    self.NormA[key] += value
                else:
                    self.NormA[key] = value

        for layer in self.interLayers:
            for key, value in layer.NormA.items():
                if key in self.NormA:
                    self.NormA[key] += value
                else:

                    self.NormA[key] = value

    def updateCumulativeRejectance(self):

        """
        Update the cumulative rejectance of multi layer network
        as R is row stochastic matrix
        :return:
        """

        for layer in self.layers:
            for key,value in layer.NormR.items():
                if key in self.NormR:
                    self.NormR[key] += value
                else:
                    self.NormR[key] = value

        for layer in self.interLayers:
            for key, value in layer.NormR.items():
                if key in self.NormR:
                    self.NormR[key] += value
                else:

                    self.NormR[key] = value

    def detCumulativeIntraLayerAcceptance(self):

        """
        Determine the cumulative Acceptance (A)

        A = ( A_delta + A_star)

        A -- Corresponsds to

        :return:
        """

        # TODO update self.A_Delta

        for layer in self.layers:
            for key,value in layer.A.items():
                if key in self.A_delta:
                    if key.split('-')[-1] in self.NormA:
                        if(self.NormA[key.split('-')[-1]] != 0):

                            self.A_delta[key] += value/( 0.0 +self.NormA[key.split('-')[-1]])

                        else:
                            self.A_delta[key] += value
                    else:
                        self.NormA[key.split('-')[-1]]=0

                else:

                    self.A_delta[key] = value

                self.g.add_weighted_edges_from([(key.split('-')[-1], key.split('-')[-2], self.A_delta[key])], color='red')

    def detCumulativeInterLayerAcceptance(self):

        """

        A* = Corresponds to Inter layer weight matrices.
        :return:
        """

        # TODO update self.A_star
        for layer in self.interLayers:
            for key,value in layer.A.items():
                if key in self.A_delta:
                    if key.split('-')[-1] in self.NormA:

                        if (self.NormA[key.split('-')[-1]] != 0):

                            self.A_delta[key] += value / (0.0 + self.NormA[key.split('-')[-1]])

                        else:
                            self.A_delta[key] += value
                    else:
                        self.NormA[key.split('-')[-1]] = 0

                else:

                    self.A_delta[key] = value

                self.g.add_weighted_edges_from([(key.split('-')[-1], key.split('-')[-2], self.A_delta[key])], color='red')

    def detCumulativeAcceptance(self,):

        """
        Determine the cumulative Acceptance (A)

        A = ( A + A*)

        A -- Corresponsds to

        :return:
        """
        # TODO update self.A


    def detCumulativeIntraLayerRejectance(self):

        """

        Determine (R) -- the effective Rejectance based on intra Layer weights.
        :return:
        """

        for layer in self.layers:
            for key,value in layer.R.items():
                if key in self.R_delta:
                    if key.split('-')[-1] in self.NormR:

                        if (self.NormR[key.split('-')[-1]] != 0):

                            self.R_delta[key] += value / (0.0 + self.NormR[key.split('-')[-1]])

                        else:
                            self.R_delta[key] += value
                    else:
                        self.NormR[key.split('-')[-1]] = 0

                else:

                    self.R_delta[key] = value

    def detCumulativeInterLayerRejectance(self):

        """
        Determine (R_star) -- the effective Rejectance based on inter Layer weights.

        :return:
        """

        # TODO update self.R_star
        for layer in self.interLayers:
            for key,value in layer.R.items():
                if key in self.R_delta:
                    if key.split('-')[-1] in self.NormR:

                        if (self.NormR[key.split('-')[-1]] != 0):

                            self.R_delta[key] += value / (0.0 + self.NormR[key.split('-')[-1]])

                        else:
                            self.R_delta[key] += value
                    else:
                        self.NormR[key.split('-')[-1]] = 0

                else:

                    self.R_delta[key] = value

    def detCumulativeRejectance(self,):

        """
        Determine the cumulative Rejectance (R)

        R = ( R_delta + R_star)

        :return:
        """

        # TODO upate self.R