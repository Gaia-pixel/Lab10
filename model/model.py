import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()  # non orientato --> solo .Graph()
        self.nodi = None
        self.idmap = {}


    def build_graph(self, anno):
        self.grafo.clear()
        # aggiungo i nodi
        self.nodi = DAO.get_countries(anno)
        self.grafo.add_nodes_from(self.nodi)
        for n in self.nodi:
            self.idmap[n.CCode] = n

        borders = DAO.get_edge(self.idmap, anno) # lista di confini
        for b in borders:
            self.grafo.add_edge(b.state1no, b.state2no)


    # creo funzione per capire numero di nodi nel grafo (da usare sempre)
    def getNumNodes(self):
        return self.grafo.number_of_nodes()
        # return len(self.idmap)

    def getNumEdges(self):
        return self.grafo.number_of_edges()

    def getNumeroConfinanti(self, v):
        return len(list(self.grafo.neighbors(v)))

    def getNumConnesse(self):
        return nx.number_connected_components(self.grafo)
