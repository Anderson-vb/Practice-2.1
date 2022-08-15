from re import template
from derive import *
from state import State
from transition import Transition

class DFA:

    def __init__(self):
        self.states = []

    def get_states(self):
        return self.states

    def set_names(self):
        for i in range(len(self.states)):
            self.states[i].set_name('q' + str(i))

    def create_dfa(self, initial_state: State):
        
        alphabet = get_alphabet(initial_state.get_regex())

        states = list(map(lambda x: State(derive(initial_state.get_regex(), x)), alphabet))

        for i in range(len(alphabet)):
            initial_state.set_transition(Transition(alphabet[i], states[i]))

        for current_state in states:
            possible_states = list(map(lambda x: State(derive(current_state.get_regex(), x)), alphabet))

            for i in range(len(possible_states)):
                for j in states:
                    new_state = True
                    if possible_states[i].get_regex() == j.get_regex():
                        current_state.set_transition(Transition(alphabet[i], j))
                        new_state = False
                        break
                
                if new_state:
                    states.append(possible_states[i])
                    current_state.set_transition(Transition(alphabet[i], possible_states[i]))

        states.insert(0, initial_state)
        self.states = states
        self.set_names()

