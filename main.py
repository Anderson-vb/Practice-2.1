from afd import AFD
from estado import Estado

regex = input('Ingresa la expresión regular: ')
state = Estado(regex)
dfa = AFD()
dfa.crear_afd(state)
dfa.mostrar_estados()
print(dfa.verificar_expresion('aba'))
