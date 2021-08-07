pessoasepeso = []
dados = []
maiorpeso = menorpeso = 0
nomemaior = []
nomemenor = []
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if len(pessoasepeso) == 0:
        menorpeso = maiorpeso = dados[1]
    if dados[1] < menorpeso:
        menorpeso = dados[1]
        nomemenor.append(dados[0])
    if dados[1] > maiorpeso:
        maiorpeso = dados[1]
        nomemaior.append(dados[0])
    n = str(input('Deseja continuar? [S/N]: '))
    pessoasepeso.append(dados[:])
    dados.clear()
    if n in 'Nn':
        break
print(f'A quantidade de pessoas registradas foi de {len(pessoasepeso)}')
print(f'O maior peso é de {maiorpeso}Kg. Peso de', end=' ')
for c in pessoasepeso:
    if c[1] == maiorpeso:
        print(c[0], end=' ')
print()
print(f'O menor peso é de {menorpeso}Kg. Peso de', end=' ')
for c in pessoasepeso:
    if c[1] == menorpeso:
        print(c[0], end=' ')