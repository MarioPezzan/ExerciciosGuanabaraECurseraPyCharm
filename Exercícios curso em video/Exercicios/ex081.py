list = []
while True:
    list.append(int(input('Digite um valor: ')))
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if stop == 'N':
        break
print(f'Você digitou {len(list)} elementos')
list.sort(reverse=True)
print(f'Os valores em ordem decrescente {list}')
if list.count(5) >= 1:
    print('O valor 5 faz parte da lista')
else: print('O valor 5 não foi encontrado na lista')

#or
if 5 in list:
    print('O valor 5 faz parte da lista')
else: print('O valor 5 não foi encontrado na lista')
