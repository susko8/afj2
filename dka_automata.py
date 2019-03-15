class DKAutomata:
    def __init__(self, states, symbols):
        self.states = states
        self.symbols = symbols

    def __repr__(self):
        s = 'DKA: \n'
        for i in self.states:
            for sy in self.symbols:
                s += i.__repr__() + ' edge ' + sy + ' to ' + i.edges[sy].__repr__() + '\n'
        return s

    def validate_string(self):
        return 0