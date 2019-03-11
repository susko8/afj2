#!/usr/bin/env python

import freader as fr
import functions as fns
from nka_state import NKAState
from nka_automata import NKAutomata

filecontent = fr.read_file()

# inicializacia klucovych premennych NKA
number_of_states = int(filecontent[0])
number_of_input_alphabet_symbols = int(filecontent[1])
nkastates = {}

# nacitanie stavov a inicializacia prislusnych tried 2 je pocet vseobecnych parametrov
for i in range(2, 2 + number_of_states):
    parsed_state = filecontent[i].split(' ')
    if len(parsed_state) == 1:
        nkastates[parsed_state[0]] = NKAState(parsed_state[0])
    else:
        if parsed_state[1] == 'I':
            s = NKAState(parsed_state[0])
            s.is_initial = True
            nkastates[parsed_state[0]] = s
        if parsed_state[1] == 'F':
            s = NKAState(parsed_state[0])
            s.is_accepting = True
            nkastates[parsed_state[0]] = s
        else:
            s = NKAState(parsed_state[0])
            s.is_accepting = True
            s.is_initial = True
            nkastates[parsed_state[0]] = s

# nacitanie symbolov
symbols = []
for i in range(2 + number_of_states, 2 + number_of_states + number_of_input_alphabet_symbols):
    symbols.append(filecontent[i])

# nacitanie prechodov
for i in range(2 + number_of_states + number_of_input_alphabet_symbols, len(filecontent)):
    parsed_edge = filecontent[i].split(',')
    nkastates[parsed_edge[0]].edges[parsed_edge[1]].append(parsed_edge[2])

nka = NKAutomata(nkastates, symbols)
print(nkastates['q0'])
# print(fns.get_state(nka.states, 'q1'))

# TODO bude treba mapu na jednotlive vrcholy ? pevne verim ze nie funkcia get_states to zarucuje


# zapis vysledku
# fr.write_result_to_file(nka.__repr__())
