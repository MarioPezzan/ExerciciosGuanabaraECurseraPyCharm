list = []
expr = str(input('Digite uma expressão: '))
for sim in expr:
    if sim == '(':
        list.append('(')
    elif sim == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            print('Sua expressão está errada')
            break
if len(list) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')