#!/usr/bin/env python

import freader as fr
from nka_state import NKAState
from nka_automata import NKAutomata

filecontent = fr.read_file()

# inicializacia klucovych premennych NKA
number_of_states = int(filecontent[0])
number_of_input_alphabet_symbols = int(filecontent[1])
nkastates = []

# nacitanie stavov a inicializacia prislusnych tried
for i in range(2, 2 + number_of_states):
    parsed_state = filecontent[i].split(' ')
    if len(parsed_state) == 1:
        nkastates.append(NKAState(parsed_state[0]))
    else:
        if parsed_state[1] == 'I':
            s = NKAState(parsed_state[0])
            s.is_initial = True
            nkastates.append(s)
        if parsed_state[1] == 'F':
            s = NKAState(parsed_state[0])
            s.is_accepting = True
            nkastates.append(s)
        else:
            s = NKAState(parsed_state[0])
            s.is_accepting = True
            s.is_initial = True
            nkastates.append(s)

# TODO read edges and init them
nka = NKAutomata(nkastates)

# zapis vysledku
# fr.write_result_to_file(nka.__repr__())
