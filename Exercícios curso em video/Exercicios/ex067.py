n = cont = 0
while True:
    if cont == 0:
        n = int(input('Qual tabuada você deseja? '))
        if n < 0:
            break
    cont += 1
    print(f'{cont} X {n} = {n * cont}')
    if cont == 10:
        cont = 0
print('acabou')

#forma alternativa
n = cont = 0
while True:
    for cont in range(0, 11):
        print(f'{cont} X {n} = {n * cont}')
    if n < 0:
        break
print('acabou')