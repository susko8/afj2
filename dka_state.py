from collections import defaultdict


class DKAState:
    def __init__(self, states):
        self.states = states
        self.are_initial = False
        self.are_accepting = False
        self.edges = defaultdict(list)

    def add_edge(self, symbol, to_edge_states):
        self.edges[symbol] = to_edge_states

    def __repr__(self):
        to_string = ''
        for state in self.states:
            to_string += state.index + ' '
        return to_string

    def __eq__(self, other):
        return self.states == other.states

    def __hash__(self):
        return id(self)
