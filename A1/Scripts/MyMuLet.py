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

    Amatrix = {}
    NormA_delta = {}

    AStarmatrix = {}
    NormA_star = {}

    # Rejectance Ratio
    R = {}
    NormR = {}

    Rmatrix = {}
    NormR_delta = {}

    RStarmatrix = {}
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

        if layers is not None:
             self.layers = layers
        if weights is not None:
            self.weights = weights

        self.getGenericGraphfromLayers()
        """
        self.detCumulativeIntraLayerAcceptance(layers[0],layers[1])
        self.detCumulativeInterLayerAcceptance(layers[0],layers[1])
        self.detCumulativeAcceptance()

        self.detCumulativeIntraLayerRejectance(layers[0], layers[1])
        self.detCumulativeInterLayerRejectance(layers[0], layers[1])
        self.detCumulativeRejectance()

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


    def detCumulativeIntraLayerAcceptance(self,lhs,rhs):

        """
        Determine the cumulative Acceptance (A)

        A = ( A_delta + A_star)

        A -- Corresponsds to




        :return:
        """
        for key in lhs.keys():
            # auto-merge for missing key on right-hand-side.
            self.Amatrix[key]=lhs[key]
            if (key in rhs):
                self.Amatrix[key] = self.Amatrix[key]+rhs[key]
                # on collision, invoke custom merge function.
            else:
                self.Amatrix[key] = lhs[key]
        for key in rhs.keys():
            # auto-merge for missing key on left-hand-side.
            if (not key in lhs):
                self.Amatrix[key] = rhs[key]
        return self.Amatrix
    # TODO update self.A_Delta

    def detCumulativeInterLayerAcceptance(self,lhs,rhs):

        """
        A* = Corresponds to Inter layer weight matrices.
        :return:
        """

        for key in lhs.keys():
            # auto-merge for missing key on right-hand-side.

            if (key in rhs):
                self.AStarmatrix[key] = 1
                # on collision, invoke custom merge function.
            else:
                self.AStarmatrix[key] = 0
        for key in rhs.keys():
            # auto-merge for missing key on left-hand-side.
            if (key in lhs):
                self.AStarmatrix[key] = 1
                # on collision, invoke custom merge function.
            else:
                self.AStarmatrix[key] = 0
        return self.AStarmatrix


    def detCumulativeAcceptance(self,):

        """
        Determine the cumulative Acceptance (A)

        A = ( A + A*)

        A -- Corresponsds to

        :return:
        """
        # TODO update self.A
        for key in self.Amatrix:
            self.Amatrix[key]=self.AStarmatrix[key]*self.Amatrix[key]
            #print(str(key)," : ",str(self.Amatrix[key]))
        return self.Amatrix

    def detCumulativeIntraLayerRejectance(self,lhs,rhs):

        """

        Determine (R) -- the effective Rejectance based on intra Layer weights.


        :return:
        """

        # TODO update self.R_delta

        for key in lhs.keys():
            # auto-merge for missing key on right-hand-side.
            self.Rmatrix[key] = lhs[key]
            if (key in rhs):
                self.Rmatrix[key] = self.Rmatrix[key] + rhs[key]
                # on collision, invoke custom merge function.
            else:
                self.Rmatrix[key] = lhs[key]
        for key in rhs.keys():
            # auto-merge for missing key on left-hand-side.
            if (not key in lhs):
                self.Rmatrix[key] = rhs[key]
        return self.Rmatrix

    def detCumulativeInterLayerRejectance(self,lhs,rhs):

        """
        Determine (R_star) -- the effective Rejectance based on inter Layer weights.

        :return:
        """

        # TODO update self.R_star

        for key in lhs.keys():
            # auto-merge for missing key on right-hand-side.

            if (key in rhs):
                self.RStarmatrix[key] = 1
                # on collision, invoke custom merge function.
            else:
                self.RStarmatrix[key] = 0
        for key in rhs.keys():
            # auto-merge for missing key on left-hand-side.
            if (key in lhs):
                self.RStarmatrix[key] = 1
                # on collision, invoke custom merge function.
            else:
                self.RStarmatrix[key] = 0
        return self.RStarmatrix

    def detCumulativeRejectance(self,):

        """
        Determine the cumulative Rejectance (R)

        R = ( R_delta + R_star)

        :return:
        """

        # TODO upate self.R
        for key in self.Rmatrix:
            self.Rmatrix[key] = self.RStarmatrix[key] * self.Rmatrix[key]
            print(str(key), " : ", str(self.Rmatrix[key]))
        return self.Rmatrix