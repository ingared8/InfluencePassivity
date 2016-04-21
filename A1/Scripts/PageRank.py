from pylab import plot,show
from ReadGraphFile import *

class PageRank():

    # -- Graph
    g = None

    # Acceptance Ratio
    # G(i,j) = 1 if there is an directed edge from i to j
    A = {}

    # Authority Scores
    a = {}

    # Hub Scores
    h = {}

    def __init__(self,filename, directional= True):

        """

        :param filename: filename in which data is present
        :param directional: Boolean -- Whether Graph is directed (True) or not (False)
        :return: None ( this is simply constructor)
        """

        # Create Graph from file
        self.g =  readGraphfromFile(filename=filename, directional= directional, weight=False)

    def modifyGraph(self,g):
        self.g = g

    """
    ** Not required **

    def calculateTheEdgeMatrix(self):

        ""
        Acceptance rate defined as

                      w(i,j)
        u(i,j) =  ---------------
                    Sum(w(k,j))

        Cumulative Acceptance is defined as Sum(w(k,j))

        for all i E (V, nodes), (i,j) E (E, Edges), (k,j) E (E, Edges)

        :return: None
        ""


        for nodej in self.g.nodes():
            for edge in self.g.out_edges(nodej):
                self.A[edge[0] + "-"+edge[1]] = 1.0

    """

    def detAuthorityScores(self, h):

        """
        a(p) = Sigma ( h(q,p) for all (q,p) belongs to edges
        :return:
        """

        a = {}
        for node in self.g.nodes():
            weight = 0.0
            for edge in self.g.in_edges(node):
                weight += h[edge[0]]
            a[node] = weight
        return a

    def detHubScores(self,a):

        """
        h(p) = Sigma ( a(p,q) for all (p,q) belongs to edges

        :return:
        """

        h = {}
        for node in self.g.nodes():
            weight = 0.0
            for edge in self.g.out_edges(node):
                weight += a[edge[1]]
            h[node] = weight
        return h


    def pageRankAlgorithm(self, m= 1000):
        """
        :return:
        """
        # TODO ( Write up for function)

        for node in self.g.nodes():
            self.a[node] = 1
            self.h[node] = 1

        iter =1
        error = 100
        errorLimit = 0.01
        aerror = 0.0
        herror = 0.0
        Errors = []
        aErrors = []
        hErrors = []
        iters = []

        while ( (iter < m) & (error > errorLimit)):

            a = self.detAuthorityScores(self.h)
            h = self.detHubScores(self.a)
            sum_hh = np.sqrt(np.sum([i*i for i in h.values()]))
            sum_aa = np.sqrt(np.sum([i*i for i in a.values()]))
            for node in self.g.nodes():
                avalue = a[node]/(sum_aa + 0.0)
                aerror += abs(avalue - self.a[node])
                self.a[node] = avalue
                hvalue = h[node]/(sum_hh + 0.0)
                herror += abs(hvalue - self.h[node])
                self.h[node] = hvalue

            error = (aerror/sum_aa) + (herror/sum_hh)
            Errors.append(error)
            aErrors.append((aerror/sum_aa))
            hErrors.append((herror/sum_hh))
            iters.append(iter)
            iter += 1
            if (iter%1 == 0):
                print "iter " , iter, "Asum ", sum_aa, 'H sum', sum_hh , self.a.values(), "h", self.h.values()
        plot(iters,Errors,'r')
        plot(iters,aErrors,'b*')
        plot(iters,hErrors,'g.')
        show()

    def run(self):
        """

        :return:
        """
        # TODO (function description)

        print " Calculate Page Rank Algorithm"
        self.pageRankAlgorithm()

