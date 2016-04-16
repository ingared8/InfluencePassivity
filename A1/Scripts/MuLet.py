__author__ = "ingared"

import networkx as nx
from IP import InfluencePassivity

class MuLet():

    """"
    A multi layer network.
    The same network showing different behaviours can be best represented using a multi layer network.
    """

    layers = []
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


    def __init__(self,layers = None, weights = None):

        """
        Construct a Mulet with a list of individual layers.
        weights represent the inter layer edges between different layers.
        :return: None
        """
        if layers is not None:
             self.layers = layers
        if weights is not None:
            self.weights = weights

        #self.getGenericGraphfromLayers()

    def update(self):

        filenames = ["/home/ingared/Documents/NS_IP/A1/Data/gnutella/Random2.txt", "/home/ingared/Documents/NS_IP/A1/Data/gnutella/Random3.txt"]
        self.layers = []
        for filename in filenames:
            self.layers.append(InfluencePassivity(filename,weight=True))

        self.getGenericGraphfromLayers()

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
                key = edge[0] + "_" + edge[1]
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

    def updateCumulativeAcceptance(self):

        """
        Update the total acceptance from i
        as A is column stochastic matrix
        :return:
        """
        for layer in self.layers:
            for key,value in layer.NormA.iteritems():
                self.NormA[key] += value


    def updateCumulativeRejectance(self):

        """
        Update the cumulative rejectance of multi layer network
        as R is row stochastic matrix
        :return:
        """

        for layer in self.layers:
            for key,value in layer.NormR.iteritems():
                self.NormR[key] += value

    def detCumulativeIntraLayerAcceptance(self):

        """
        Determine the cumulative Acceptance (A)

        A = ( A_delta + A_star)

        A -- Corresponsds to

        :return:
        """

        # TODO update self.A_Delta


        for layer in self.layers:
            for key,value in layer.A.iteritems():
                self.A_delta[key] += value/( 0.0 +self.NormA[key.split('-')[-1]])

    def detCumulativeInterLayerAcceptance(self):

        """

        A* = Corresponds to Inter layer weight matrices.
        :return:
        """

        # TODO update self.A_star

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
            for key,value in layer.R.iteritems():
                self.R_delta[key] += value/(0.0 + self.NormR[key.split('-')[0]])

    def detCumulativeInterLayerRejectance(self):

        """
        Determine (R_star) -- the effective Rejectance based on inter Layer weights.

        :return:
        """

        # TODO update self.R_star


    def detCumulativeRejectance(self,):

        """
        Determine the cumulative Rejectance (R)

        R = ( R_delta + R_star)

        :return:
        """

        # TODO upate self.R