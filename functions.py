import copy
from dka_state import DKAState
from nka_state import NKAState


def find_starting_state(automata):
    for index, state in automata.states.items():
        if state.is_initial:
            return state


def epsilon_clsr(automata, states, edge_name):
    automata_states = copy.deepcopy(automata.states)
    in_states = copy.deepcopy(states)
    result = []
    if edge_name == '':
        result = in_states

    for key, value in automata_states.items():
        for state in in_states:
            if key in state.edges[edge_name]:
                result.append(automata_states[key])
    for key, value in automata_states.items():
        for state in result:
            if key == state.index:
                break
            if key in state.edges[edge_name] or key in state.edges['']:
                result.append(automata_states[key])
    result = list(dict.fromkeys(result))
    result.sort(key=lambda state: state.index)
    # print('cslr_in', in_states, edge_name)
    # print('cslr_res', result)
    return result


def init_dka_states(dka_states_array):
    dka_automata_states = []
    for i in range(len(dka_states_array)):
        to_append_dka_state = DKAState(dka_states_array[i])
        for nka_state in dka_states_array[i]:
            if nka_state.is_accepting:
                to_append_dka_state.are_accepting = True
            nka_state.edges = None
        dka_automata_states.append(to_append_dka_state)
        dka_automata_states[0].are_initial = True
    return dka_automata_states


def convert_dka_table_states(table):
    for x in range(len(table)):
        for y in range(len(table[0])):
            sts = table[x][y]
            dka_sts = DKAState(table[x][y])
            for state in sts:
                if state.is_accepting:
                    dka_sts.are_accepting = True
            table[x][y] = dka_sts
    return table


def init_trap_states(table, dka_states,symlen):
    flag = False
    trap_state = DKAState([NKAState('qpasca')])
    for x in range(len(table)):
        for y in range(len(table[0])):
            if not table[x][y].states:
                table[x][y] = trap_state
                flag = True
    if flag:
        dka_states.append(trap_state)
        for i in range(symlen):
            table[i].append(trap_state)
