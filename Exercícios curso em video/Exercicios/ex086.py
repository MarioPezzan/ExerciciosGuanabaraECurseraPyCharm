lista = [[], [], []]
for p in range(3):
    for c in range(3):
        lista[p].append(int(input(f'Digite um valor [{p}, {c}]: ')))
for p in range(3):
    for c in range(3):
        print(f'[{lista[p][c]:^5}]', end='')
    print()