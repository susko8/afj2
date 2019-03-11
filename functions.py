def find_starting_state(automata):
    for index, state in automata.states.items():
        if state.is_initial:
            return state


def epsilon_clsr(state, edge):
    return 0
