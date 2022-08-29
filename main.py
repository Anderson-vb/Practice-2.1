from dfa import DFA
from state import State

regex = input('Ingresa la expresión regular: ')
state = State(regex)
dfa = DFA()
dfa.create_dfa(state)
dfa.show_states()
print(dfa.verify_string('aba'))
