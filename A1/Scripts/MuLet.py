__author__ = "ingared"

class MuLet():
    """"
    A multi layer network.
    The same network showing different behaviours can be best represented using a multi layer network.
    """

    layers = []
    weights = None

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


    def detCumulativeIP(self):
        """

        :return:
        """

        # TODO ( write functionality)
        pass