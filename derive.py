from functools import reduce

alphabet = []

def set_alphabet(regex):
    global alphabet
    alphabet.clear()
    alphabet = [i for i in regex if i != '+' and i != '*' and i != '(' and i != ')']

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
    
def v(regex):

    if regex == 'ε':
        return 'ε'

    elif regex == '∅':
        return '∅'

    elif regex in alphabet:
        return '∅'

    elif '+' in regex:
        temp = regex.split('+')
        temp_2 = list(map(v, temp))
        return simplify('+'.join(temp_2))

    elif len(regex) > 1 and not (len(regex) == 2 and regex.endswith('*')):
        temp = [regex[i] + regex[i + 1] if i < len(regex) - 1 and regex[i + 1] == '*' else regex[i] for i in range(len(regex))]
        temp_2 = [i for i in temp if i != '*']
        temp_3 = list(map(v, temp_2))
        return simplify(''.join(temp_3))

    elif '*' in regex:
        return 'ε'   

def derive(regex, character):
    
    if regex == 'ε' or regex == '∅':
        return '∅'

    elif regex == character:
        return 'ε'

    elif len(regex) == 1:
        return '∅'

    elif '+' in regex:
        temp = regex.split('+')
        temp_2 = list(map(lambda x: derive(x, character), temp))
        return simplify('+'.join(temp_2))
    
    # TODO Arreglar esta shitex
    elif len(regex) > 1 and not (len(regex) == 2 and regex.endswith('*')):
        temp = [regex[i] + regex[i + 1] if i < len(regex) - 1 and regex[i + 1] == '*' else regex[i] for i in range(len(regex))]
        temp_2 = [i for i in temp if i != '*']
        temp_4 = reduce(lambda x, y: derive(x, character) + y + '+' + v(x) + derive(y), temp_2)
        temp_3 = list(map(lambda x: derive(x, character), temp_2))
        return simplify(''.join(temp_3))

derive('ab', 'a')