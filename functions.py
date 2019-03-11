def get_state(states, name):
    for i in range(0, len(states)):
        if states[i].index == name:
            return states[i]


def epsilon_clsr(clsr_arg):
    return len(clsr_arg)
