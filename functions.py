import copy


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
    # TODO one more loop for check for resutl neighbors
    result = list(dict.fromkeys(result))
    result.sort(key=lambda state: state.index)
    print('cslr_in', in_states, edge_name)
    print('cslr_res', result)
    return result
