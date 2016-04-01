import networkx as nx
from pylab import plot,show
import matplotlib.pyplot as plt
from osm import *

def download_osm(left,bottom,right,top):
    """ Return a filehandle to the downloaded data."""
    from urllib import urlopen
    fp = urlopen( "http://api.openstreetmap.org/api/0.5/map?bbox=%f,%f,%f,%f"%(left,bottom,right,top) )
    return fp


def read_osm(filename_or_stream, only_roads=True):
    """Read graph in OSM format from file specified by name or by stream object.

    Parameters
    ----------
    filename_or_stream : filename or stream object

    Returns
    -------
    G : Graph

    Examples
    --------


    """
    osm = OSM(filename_or_stream)
    G = nx.Graph()

    for w in osm.ways.itervalues():
        if only_roads and 'highway' not in w.tags:
            continue
        G.add_path(w.nds, id=w.id, data=w)
    for n_id in G.nodes_iter():
        n = osm.nodes[n_id]
        G.node[n_id] = dict(data=n)
    return G

G= read_osm(download_osm(-122.33,47.60,-122.31,47.61))
plot([G.node[n]['data'].lat for n in G], [G.node[n]['data'].lon for n in G], ',')
show()

