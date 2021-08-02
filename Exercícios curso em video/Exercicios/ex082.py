list = []
while True:
    list.append(int(input('Digite um número: ')))
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N]: ')).strip()[0].upper()
    if stop == 'N':
        break
impares = list[:]
pares = list[:]
for c in list:
    if c % 2 == 0:
        impares.remove(c)
    if c % 2 == 1:
        pares.remove(c)
print(f'A lista completa {list}')
print(f'A lista de pares {pares}')
print(f'A lista de ímpares {impares}')
