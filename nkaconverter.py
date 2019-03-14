#!/usr/bin/env python

import pandas as pd
import freader as fr
import functions as fns
import numpy as np
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

dka_table = [[] for j in range(len(symbols))]

dka_states_array = []

# test = fns.epsilon_clsr(nka, [nka.states['q0'], nka.states['q1']], 'a')
first_index = fns.epsilon_clsr(nka, [fns.find_starting_state(nka)], '')


dka_states_array.append(first_index)

print('initial_dka_state',first_index)
# foo = fns.epsilon_clsr(nka, [fns.find_starting_state(nka)], 'b')
n_of_validated_rows = 0

while True:
    flag = False
    to_append = []
    for i in range(len(symbols)):
        state = fns.epsilon_clsr(nka, dka_states_array[len(dka_states_array) - 1], symbols[i])
        dka_table[i].append(state)
        to_append.append(state)
    for state in to_append:
        if state in dka_states_array or not state:
            flag = True
        else:
            dka_states_array.append(state)
            flag = False
    n_of_validated_rows += 1
    if flag and n_of_validated_rows == len(dka_states_array):
        break

# noinspection PyUnreachableCode
print('list',dka_states_array)
print('table',dka_table)

# print(fns.epsilon_clsr(nka, [fns.find_starting_state(nka)], ''))
# zapis vysledku
# fr.write_result_to_file(nka.__repr__())


# zatial nepotrebny kod

# closure_table = pd.DataFrame(columns=nka.symbols)
# closure_table.loc[fns.epsilon_clsr(nka, [fns.find_starting_state(nka)], '')] = 0
# closure_table.loc[first_index] = 0
# closure_table.loc[nka.states['q1']] = 1
# closure_table.at[[fns.find_starting_state(nka)], 'a'] = 1
# row_indexes = closure_table.index
# print(row_indexes)

# print(closure_table)
#
