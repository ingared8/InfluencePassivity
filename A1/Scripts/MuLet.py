__author__ = "ingared"

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

    A_star = {}
    NormA_star = {}

    # Rejectance Ratio
    R = {}
    NormR = {}

    R_star = {}
    NormR_star = {}

    # Influeence Scores
    I = {}
    NormI = {}

    # Passivity Scores
    P = {}
    NormP = {}



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

    def detCumulativeIntraLayerAcceptance(self,):

        """
        Determine the cumulative Acceptance (A)

        A = ( A + A*)

        A -- Corresponsds to

        :return:
        """

    def detCumulativeAcceptance(self,):

        """
        Determine the cumulative Acceptance (A)

        A = ( A + A*)

        A -- Corresponsds to

        :return:
        """

    def detCumulativeRejectance(self,):

        """
        Determine the cumulative Acceptance (A)

        A = ( A + A*)

        A -- Corresponsds to

        :return:
        """


    def detCumulativeInterLayerAcceptance(self):

        """

        A* = Corresponds to Inter layer weight matrices.
        :return:
        """

    def detCumulativeIntraLayerRejectance(self):

        """

        Determine (R) -- the effective Rejectance based on intra Layer weights.


        :return:
        """

    def detCumulativeInterLayerRejectance(self):

        """
        Determine (R_star) -- the effective Rejectance based on inter Layer weights.

        :return:
        """


    def detCumulativeIP(self):

        """

        :return:
        """

        # TODO ( write functionality)
        pass
