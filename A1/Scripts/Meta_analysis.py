import numpy as np
import os

dir = "A1/output"

def savefigure( dict, name, type ):
    try:
        import matplotlib.pyplot as plt
        plt.figure(1)
        plt.plot(dict.keys(), dict.values(),'b*')
        plt.title(name)
        filename = (type + name + ".jpg")
        plt.savefig(filename)
        plt.close()
    except:
        print "Matplotlib is not available"

    try:
        values = dict.values()
        print type, name
        print " Mean  : " , np.mean(values)
        print " std/Mean   : " , np.std(values)/np.mean(values)
        print " var/mean   : " , np.var(values)/np.mean(values)
    except:
        pass

def getCorrelation(dict1, dict2):
    keys = [key for key in dict1.keys() if key in dict2.keys()]
    arr1 = [dict1[key] for key in keys]
    arr2 = [dict2[key] for key in keys]
    cor = np.corrcoef(arr1,arr2)
    print cor[0][1]

# For wiki
for type in ['gnutella','facebook','quantum' , 'wiki']:

    try:
        # Load DegreeCentrality
        degCen = np.load(os.path.join(dir, type, "degreeCentrality.npz"))
        if (len(degCen.files) == 4):
             inDegreeCentrality = degCen['arr_2'].item()
             outDegreeCentrality = degCen['arr_3'].item()
             savefigure(inDegreeCentrality,'InDegreeCentrality', type=type)
             savefigure(outDegreeCentrality, 'outDegreeCentrality',type=type)
        elif ( len(degCen.files)== 2):
            degreeCentrality = degCen['arr_1'].item()
            savefigure(degreeCentrality,'degreeCentrality', type=type)
        else:
            pass

        # Load Closeness Centrality
        cloCen = np.load(os.path.join(dir, type, "closenessCentrality.npz"))
        if (len(cloCen.files) == 1):
             closenessCentrality = cloCen['arr_0'].item()
             savefigure(closenessCentrality,'closenessCentrality', type=type)

        # Load Harmonic Centrality
        harCen = np.load(os.path.join(dir,type,"harmonicCentrality.npz"))
        if (len(harCen.files) == 1):
             harmonicCentrality = harCen['arr_0'].item()
             savefigure(harmonicCentrality,'harmonicCentrality', type=type)

        # Load BetweenNess Centrality
        betCen = np.load(os.path.join(dir,type,"betweennessCentrality.npz"))
        if (len(harCen.files) == 1):
             betweennessCentrality = betCen['arr_0'].item()
             savefigure(betweennessCentrality,'betweennessCentrality', type=type)

        # Load Clustering Cofficient
        cluCof = np.load(os.path.join(dir,type,"clusteringCofficient.npz"))
        if (len(harCen.files) >= 1):
             clusteringCofficient = cloCen['arr_0'].item()
             savefigure(clusteringCofficient,'clusteringCofficient', type=type)

        # Load Eigen Vector Centrality
        eigVec =  np.load(os.path.join(dir,type,"eigenVector.npz"))
        if (len(eigVec.files) >= 1) :
            eigenVector = eigVec['arr_0'].item()
            savefigure(eigenVector,'eigenVector',type=type)

        # Page Rank Centrality
        pagRan =  np.load(os.path.join(dir,type,"pageRank.npz"))
        if ( len(pagRan.files) >= 1):
            pageRank = pagRan['arr_0'].item()
            savefigure(pageRank,'pageRank',type=type)


        # Correlation among degree and others

        print " Calculating Correlation matrix between various measures in order of "
        print "Degree Centrality against"
        print "Harmonic Centrality, Betweenness Centrality, Clustering Cofficient, pagerank, eigenVector respectively"

        getCorrelation(inDegreeCentrality,harmonicCentrality)
        getCorrelation(inDegreeCentrality,betweennessCentrality)
        getCorrelation(inDegreeCentrality,clusteringCofficient)
        getCorrelation(inDegreeCentrality,pageRank)
        getCorrelation(inDegreeCentrality,eigenVector)

        print "harmonic Centrality"
        print "Betweenness Centrality, Clustering Cofficient, pagerank, eigenVector respectively"

        getCorrelation(harmonicCentrality,betweennessCentrality)
        getCorrelation(harmonicCentrality,clusteringCofficient)
        getCorrelation(harmonicCentrality,pageRank)
        getCorrelation(harmonicCentrality,eigenVector)

        print "Betweenness Centrality aginst "
        print "Clustering Cofficient, pagerank, eigenVector respectively"

        getCorrelation(betweennessCentrality,clusteringCofficient)
        getCorrelation(betweennessCentrality,pageRank)
        getCorrelation(betweennessCentrality,eigenVector)

        print "Clustering Cofficient" , " aginst "
        print "pagerank" , "eigenVector respectively"

        getCorrelation(clusteringCofficient,pageRank)
        getCorrelation(clusteringCofficient,eigenVector)

        print "pagerank" , " aginst "
        print "eigenVector "

        getCorrelation(pageRank,eigenVector)

    except:
        pass