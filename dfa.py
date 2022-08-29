from random import getstate
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

        temp = list(map(lambda x: State(read_expresion(initial_state.get_regex(), x)), alphabet))

        for i in range(len(alphabet)):
            if initial_state.get_regex() == temp[i].get_regex():
                initial_state.set_transition(Transition(alphabet[i], initial_state))
            else:
                initial_state.set_transition(Transition(alphabet[i], temp[i]))

        states = []
        states.append(temp[0])
        for i in temp:
            esta = False
            for j in states:
                if i.get_regex() == j.get_regex():
                    esta = True
            if not esta:
                states.append(i)

        for current_state in states:
            possible_states = list(map(lambda x: State(read_expresion(current_state.get_regex(), x)), alphabet))

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
        
        
    def verify_string(self, text):

        regex = self.states[0].get_regex()

        if regex == text:
            return True

        while text != 'ε':
            regex = derive(regex, text[0])
            text = read_expresion(text, text[0])
            
        print(regex)
        print(text)

        if regex == text:
            return True

        elif len(regex) == 2 and regex.endswith('*'):
            return True


    def show_states(self):
        text = ''
        for x in self.states:
            print('\n' + x.get_name() + ' ' + x.get_regex())
            text = text + x.get_name() + ': ' + x.get_regex() + '\n'
            for y in x.get_transition():
                text = text +  y.get_character() + ' -> ' + y.get_state().get_regex() + '\n'
                print(y.get_character() + ' -> ' + y.get_state().get_regex())
        return text


