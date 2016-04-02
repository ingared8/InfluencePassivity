__author__ = "ingared"

import networkx as nx


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

        self.getGenericGraphfromLayers()

    def getGenericGraphfromLayers(self):

        """
        Generate a graph which covers every node of the multi layers
        :return:
        """
        self.g = nx.DiGraph()

        for layer in self.layers:
            for node in layer.g.nodes():
                if not (self.g.has_node(node)):
                    self.g.add_node(node)
                else:
                    pass


    def detCumulativeIntraLayerAcceptance(self,):

        """
        Determine the cumulative Acceptance (A)

        A = ( A_delta + A_star)

        A -- Corresponsds to

        :return:
        """

        # TODO update self.A_Delta

    def detCumulativeInterLayerAcceptance(self):

        """

        A* = Corresponds to Inter layer weight matrices.
        :return:
        """


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

        # TODO update self.R_delta


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