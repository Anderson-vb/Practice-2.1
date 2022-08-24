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
            if initial_state.get_regex() == states[i].get_regex():
                initial_state.set_transition(Transition(alphabet[i], initial_state))
            else:
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
                    elif possible_states[i].get_regex() == initial_state.get_regex():
                        current_state.set_transition(Transition(alphabet[i], initial_state))
                        new_state = False
                        break
                
                if new_state:
                    states.append(possible_states[i])
                    current_state.set_transition(Transition(alphabet[i], possible_states[i]))
 
        for i in range(len(states)):
            if states[i].get_regex() == initial_state.get_regex():
                states.remove(states[i])
                i = 0

        states.insert(0, initial_state)
        self.states = states
        self.set_names()

    def show_states(self):
        text = ''
        for x in self.states:
            print('\n' + x.get_name() + ' ' + x.get_regex())
            text = text + x.get_name() + ': ' + x.get_regex() + '\n'
            for y in x.get_transition():
                text = text +  y.get_character() + ' -> ' + y.get_state().get_regex() + '\n'
                print(y.get_character() + ' -> ' + y.get_state().get_regex())
        return text



