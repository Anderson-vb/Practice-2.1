from dfa import DFA
from state import State

regex = input('Ingresa la expresión regular: ')
state = State(regex)
dfa = DFA()
dfa.create_dfa(state)
dfa.show_states()
dfa.verify_string('a')
