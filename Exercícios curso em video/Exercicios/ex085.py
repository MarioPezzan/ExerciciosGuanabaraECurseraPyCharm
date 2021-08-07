dados = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        dados[1].append(n)
    else:
        dados[0].append(n)
dados[1].sort()
dados[0].sort()
print(f'Os valores pares digitados foram: {dados[1]}')
print(f'Os valores impares digitados foram: {dados[0]}')