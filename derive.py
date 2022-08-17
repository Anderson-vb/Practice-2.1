alphabet = []

def get_alphabet(regex):
    global alphabet
    alphabet.clear()
    alphabet = [i for i in regex if i != '+' and i != '*' and i != '(' and i != ')']
    return alphabet

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

def derive(regex, character):

    regex = regex.replace(' ', '')
    
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
    
    elif len(regex) > 1 and not (len(regex) == 2 and regex.endswith('*')):
        return regex[1:] if regex.startswith(character) else '∅'

    elif '*' in regex:
        return simplify(derive(regex[:-1], character) + '('  + regex + ')')
