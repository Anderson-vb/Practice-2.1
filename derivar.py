alfabeto = []

def get_alfabeto(regex):
    caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    global alfabeto
    alfabeto.clear()
    alfabeto = [i for i in regex if i in caracteres_permitidos]
    temp = []
    for x in alfabeto:
        if x not in temp:
            temp.append(x)
    return temp

def eliminar_epsilon(regex):
    temp = ''
    for i in regex:
        if i != 'ε':
            temp = temp + i
    return temp if len(temp) >= 1 else 'ε'
    
def simplificar(regex):
    temp = regex.split('+')
    temp_2 = [i for i in temp if '∅' not in i]
    return '∅' if len(temp_2) == 0 else '+'.join([eliminar_epsilon(i) for i in temp_2])

# Esta funcion retorna la derivada de una expresión regular con respecto a un caracter
def derivar(regex, character):

    regex = regex.replace(' ', '') 

    if regex.startswith('('):
        regex = regex[1:]
        temp = ''
        temp_2 = ''
        antes = True
        for x in regex:
            if x == ')' and antes: 
                antes = False
                continue
            if antes:
                temp = temp + x
            elif not antes:
                temp_2 = temp_2 + x

        if temp_2.startswith('*'):
            temp_2 = temp_2[1:]
            return simplificar(simplificar(derivar(temp, character)) + '(' + temp + ')*' + temp_2 if derivar(temp, character) != '∅' else '∅')
        else:
            temp_3 = simplificar(derivar(temp, character))
            temp_4 = temp_3 + temp_2
            return simplificar(temp_4)
    
    if regex == 'ε' or regex == '∅':
        return '∅'

    elif regex == character:
        return 'ε'

    elif len(regex) == 1:
        return '∅'

    elif '+' in regex and not '(' in regex:
        temp = regex.split('+')
        temp_2 = list(map(lambda x: derivar(x, character), temp))
        return simplificar('+'.join(temp_2))
    
    elif len(regex) > 1 and not (len(regex) == 2 and regex.endswith('*')):
        return regex[1:] if regex.startswith(character) else '∅'

    elif '*' in regex:
        return simplificar(derivar(regex[:-1], character) + '('  + regex + ')')

# Esta función se encarga de leer la expresion regular y dividirla en las subexpresiones necesarias, para 
# luego derivarlas y retornar la derivada completa de la expresion regular
def leer_expresion(regex, character):
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
        
    temp_3 = list(map(lambda x: derivar(x, character), temp_2))
    return simplificar('+'.join(temp_3))

# Esta función se encarga de verificar que la expresión regular esté correctamente escrita
def verificar_errores(regex):
    caracteres = get_alfabeto(regex)
    operadores = []
    caracteres_erroneos = []
    error = False
    texto = ''

    for x in regex:

        if x == '(' or x == ')' or x == '+' or x == '*':
            operadores.append(x)
        elif x not in caracteres:
            caracteres_erroneos.append(x)
            error = True

    if '**' in regex:
        texto = texto + 'Error: La expresion "**" no es valida \n'
        error = True
    if '++' in regex:
        texto = texto + 'Error: La expresion "++" no es valida \n'
        error = True

    for x in caracteres_erroneos:
        texto = texto + f'Error: El caracter {x} no es valido \n'

    if operadores.count('(') > operadores.count(')'):
        texto = texto + 'Error: ")" esperado \n'
        error = True
    if operadores.count('(') < operadores.count(')'):
        texto = texto + 'Error: "(" esperado \n'
        error = True

    if regex.startswith('+'):
        texto = texto + 'Error: El caracter "+" no puede ir al inicio de la expresion \n'
        error = True
    if regex.endswith('+'):
        texto = texto + 'Error: El caracter "+" no puede ir al final de la expresion \n'
        error = True

    if regex.startswith('*'):
        texto = texto + 'Error: El caracter "*" no puede ir al inicio de la expresion \n'
        error = True

    return [error, texto]
