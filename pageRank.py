import operator
import math, random, sys, csv 
from utils import parse #, print_results

class PageRank:
    def __init__(self, graph, directed):
        """
        Initialization function for class
        """
        self.graph = graph
        self.V = len(self.graph)
        self.beta = 0.85
        self.directed = directed
        self.ranks = {}
    
    def rank(self):
        for key, node in self.graph.nodes(data=True):
            if self.directed:
                self.ranks[key] = 1/float(self.V)
            else:
                self.ranks[key] = node.get('rank')

        for _ in range(20):
            for key, node in self.graph.nodes(data=True):
                rank_sum = 0
                curr_rank = node.get('rank')
                if self.directed:
                    neighbors = self.graph.out_edges(key)
                    for n in neighbors:
                        outlinks = len(self.graph.out_edges(n[1]))
                        if outlinks > 0:
                            rank_sum += (1 / float(outlinks)) * self.ranks[n[1]]
                else: 
                    neighbors = self.graph[key]
                    for n in neighbors:
                        if self.ranks[n] is not None:
                            outlinks = len(self.graph.neighbors(n))
                            rank_sum += (1 / float(outlinks)) * self.ranks[n]
            
                # actual page rank compution
                self.ranks[key] = ((1 - float(self.beta)) * (1/float(self.V))) + self.beta*rank_sum

        return pRank

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Expected input format: python pageRank.py <data_filename> <directed OR undirected>'
    else:
        filename = sys.argv[1]
        isDirected = False
        if sys.argv[2] == 'directed':
            isDirected = True

        # We load graph from csv file. We indicate wheather the graph is directed 
        # or undirected
        # The function "parse" is loaded from the module utils.py
        graph = parse(filename, isDirected)
        # Once the graph is loaded, we instantiate the PageRank() class
        pRank = PageRank(graph, isDirected)
        # Get rank for the just instantiated graph
        pRank.rank()

        # pRank.ranks is a dictionary...
        pRank_dictionary = pRank.ranks
        # whose items will be sorted according to value in descending order
        # In what follows:
        #                  key = operator.itemgetter(1) --> values of dictionary
        #                  reverse = True --> descending order

        #
        # From pRank we get an iterable that will be sorted out accordng to value
        sorted_r = sorted(pRank_dictionary.iteritems(), key=operator.itemgetter(1), reverse=True)

        # We finally iterate over sorted_r and print out results to screen...
        for tup in sorted_r:
            print '{0:30} :{1:10}'.format(str(tup[0]), tup[1])


 
