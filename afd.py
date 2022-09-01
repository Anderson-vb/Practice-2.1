from random import getstate
from derivar import *
from estado import Estado
from transicion import Transicion
from tabulate import tabulate

class AFD:

    def __init__(self):
        self.estados = []

    def get_estados(self):
        return self.estados

    def set_nombres(self):
        for i in range(len(self.estados)):
            self.estados[i].set_nombre('q' + str(i))

    # Esta función se encarga de crear todos los estados con sus respectivas transiciones
    def crear_afd(self, initial_state: Estado):
        
        alfabeto = get_alfabeto(initial_state.get_regex())

        temp = list(map(lambda x: Estado(leer_expresion(initial_state.get_regex(), x)), alfabeto))

        for i in range(len(alfabeto)):
            transicion_ya_agregada = False
            try:
                for x in initial_state.get_transiciones().copy():
                    if temp[i].get_regex() == x.get_estado().get_regex():
                        transicion_ya_agregada = True
                        initial_state.set_transicion(Transicion(alfabeto[i], x.get_estado()))
            except:
                pass

            if not transicion_ya_agregada:

                if initial_state.get_regex() == temp[i].get_regex():
                    initial_state.set_transicion(Transicion(alfabeto[i], initial_state))
                else:
                    initial_state.set_transicion(Transicion(alfabeto[i], temp[i]))

        estados = []
        estados.append(temp[0])
        for i in temp:
            temp_2 = False
            for j in estados:
                if i.get_regex() == j.get_regex():
                    temp_2 = True
            if not temp_2:
                estados.append(i)

        for estado_actual in estados:
            posibles_estados = list(map(lambda x: Estado(leer_expresion(estado_actual.get_regex(), x)), alfabeto))

            for i in range(len(posibles_estados)):
                for j in estados:
                    estado_nuevo = True
                    if posibles_estados[i].get_regex() == j.get_regex():
                        if j.get_regex() == initial_state.get_regex():
                            estado_actual.set_transicion(Transicion(alfabeto[i], initial_state))
                            estado_nuevo = False
                        else:
                            estado_actual.set_transicion(Transicion(alfabeto[i], j))
                            estado_nuevo = False
                        break
                    elif posibles_estados[i].get_regex() == initial_state.get_regex():
                        estado_actual.set_transicion(Transicion(alfabeto[i], initial_state))
                        estado_nuevo = False
                        break
                
                if estado_nuevo:
                    estados.append(posibles_estados[i])
                    estado_actual.set_transicion(Transicion(alfabeto[i], posibles_estados[i]))
 
        estados_temporales = []
        for i in range(len(estados)):
            if estados[i].get_regex() == initial_state.get_regex():
                pass
            else:
                estados_temporales.append(estados[i])

        estados_temporales.insert(0, initial_state)
        self.estados = estados_temporales
        self.set_nombres()
            
    # Esta función se encarga de validar una cadena de texto sobre el AFD 
    def verificar_expresion(self, texto):

        regex = self.estados[0].get_regex()

        if regex == texto:
            return True

        while texto != 'ε':
            regex = leer_expresion(regex, texto[0])
            texto = leer_expresion(texto, texto[0])
            
        if regex == texto:
            return True

        elif len(regex) == 2 and regex.endswith('*'):
            return True

        temp = regex.split('+')
        temp_2 = []
        expresion = ''
        parentesis = False
        for i in range(len(temp)):
            if '(' in temp[i] and not ')' in temp[i] or parentesis:
                if ')' in temp[i]:
                    if len(expresion) == 0:
                        expresion = expresion + temp[i]
                    else:
                        expresion = expresion + '+' + temp[i]
                    parentesis = False
                    temp_2.append(expresion)
                    expresion = ''
                else:
                    if len(expresion) == 0:
                        expresion = expresion + temp[i]
                    else:
                        expresion = expresion + '+' + temp[i]
                    parentesis = True
            else:
                temp_2.append(temp[i])
                parentesis = False
                expresion = ''

        for x in temp_2:
            if x.startswith('(') and x.endswith('*'):
                return True
        
        return False


    def mostrar_estados(self):
        # Crear datos
        data = []
        for x in self.estados:
            temp = []
            temp.append(x.get_nombre())
            for y in x.get_transiciones():
                temp.append(y.get_estado().get_nombre())
            data.append(temp)

        # Definir nombres de las columnas

        alfabeto = get_alfabeto(self.estados[0].get_regex())
        col_names = ['Estados']
        for x in alfabeto:
            col_names.append(x)

        return tabulate(data, headers=col_names)
