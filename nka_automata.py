class NKAutomata:
    def __init__(self, states):
        self.states = states

    def to_dka(self, symbol, to_edge_index):
        return 'konverzia'

    def __repr__(self):
        s = 'NKA: \n'
        for i in self.states:
            s +=  i.__repr__() + '\n'
        return s
