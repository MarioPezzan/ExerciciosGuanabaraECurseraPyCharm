matriz = [[], [], []]
somapares2 = somalinha3 = maiorvalor = 0
for l in range(3):
    for v in range(3):
        matriz[l].append(int(input(f'Digite o valor para [{l}, {v}]:')))
for l in range(3):
    for v in range(3):
        print(f'[{matriz[l][v]:^5}]', end='')
        if matriz[l][v] % 2 == 0:
            somapares2 += matriz[l][v]
        if v == 0:
            somalinha3 += matriz[l][2]
        if l == 1:
            if matriz[l][v] > maiorvalor:
                maiorvalor = matriz[l][v]
    print()
print(f'a soma dos valores pares é {somapares2}')
print(f'a soma dos valores da terceira coluna é {somalinha3}')
print(f'o maior valor da segunda linha é {maiorvalor}')
