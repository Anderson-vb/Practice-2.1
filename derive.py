alphabet = []

def get_alphabet(regex):
    global alphabet
    alphabet.clear()
    alphabet = [i for i in regex if i != '+' and i != '*' and i != '(' and i != ')']
    temp = []
    for x in alphabet:
        if x not in temp:
            temp.append(x)
    return temp

def remove_epsilon(regex):
    temp = ''
    for i in regex:
        if i != 'ε':
            temp = temp + i
    return temp if len(temp) >= 1 else 'ε'
    
def simplify(regex):
    temp = regex.split('+')
    temp_2 = [i for i in temp if '∅' not in i]
    return '∅' if len(temp_2) == 0 else '+'.join([remove_epsilon(i) for i in temp_2])

def remove_parenthesis(regex):
    while regex.startswith('(') and regex.endswith(')'):
        regex = regex[1:]
        regex = regex[:-1]
    return regex

def derive(regex, character):

    regex = regex.replace(' ', '') 

    if regex.startswith('('):
        regex = regex[1:]
        temp = ''
        temp_2 = ''
        before = True
        for x in regex:
            if x == ')' and before: 
                before = False
                continue
            if before:
                temp = temp + x
            elif not before:
                temp_2 = temp_2 + x

        if temp_2.startswith('*'):
            temp_2 = temp_2[1:]
            return simplify(simplify(derive(temp, character)) + '(' + temp + ')*' + temp_2 if derive(temp, character) != '∅' else '∅')
        else:
            temp_3 = simplify(derive(temp, character))
            temp_4 = temp_3 + temp_2
            return simplify(temp_4)
    
    if regex == 'ε' or regex == '∅':
        return '∅'

    elif regex == character:
        return 'ε'

    elif len(regex) == 1:
        return '∅'

    elif '+' in regex and not '(' in regex:
        temp = regex.split('+')
        temp_2 = list(map(lambda x: derive(x, character), temp))
        return simplify('+'.join(temp_2))
    
    elif len(regex) > 1 and not (len(regex) == 2 and regex.endswith('*')):
        return regex[1:] if regex.startswith(character) else '∅'

    elif '*' in regex:
        return simplify(derive(regex[:-1], character) + '('  + regex + ')')


def read_expresion(regex, character):
    #regex = remove_parenthesis(regex)
    temp = regex.split('+')
    temp_2 = []
    expression = ''
    parenthesis = False
    for i in range(len(temp)):
        if '(' in temp[i] and not ')' in temp[i] or parenthesis:
            if ')' in temp[i]:
                if len(expression) == 0:
                    expression = expression + temp[i]
                else:
                    expression = expression + '+' + temp[i]
                parenthesis = False
                temp_2.append(expression)
            else:
                if len(expression) == 0:
                    expression = expression + temp[i]
                else:
                    expression = expression + '+' + temp[i]
                parenthesis = True
        else:
            temp_2.append(temp[i])
            parenthesis = False
            expression = ''
        
    temp_3 = list(map(lambda x: derive(x, character), temp_2))
    return simplify('+'.join(temp_3))

print(derive('(a+b)a + ba', 'b'))
