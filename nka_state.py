from collections import defaultdict

class NKAState:
    def __init__(self, index):
        self.index = index
        self.is_initial = False
        self.is_accepting = False
        self.edges = defaultdict(list)

    def add_edge(self, symbol, to_edge_index):
        self.edges[symbol] = to_edge_index

    def __repr__(self):
        return 'index: ' + self.index + ',  is_initial: ' + str(self.is_initial)\
               + ', is_accepting: ' + str(self.is_accepting) + '\nedges: ' + str(self.edges)
