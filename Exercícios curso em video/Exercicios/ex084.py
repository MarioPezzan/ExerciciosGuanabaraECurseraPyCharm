pessoas = []
dados = []
contpessoas = maiorpeso = menorpeso = 0
nomemaior = []
nomemenor = []
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    n = str(input('Deseja continuar? [S/N]: '))
    pessoas.append(dados[:])
    contpessoas += 1
    dados.clear()
    if n in 'Nn':
        break
for p, c in enumerate(pessoas):
    if p == 1:
        menorpeso = pessoas[0][1]
    if c[1] <= menorpeso:
        menorpeso = c[1]
        nomemenor.append(c[0])
    if c[1] > maiorpeso:
        maiorpeso = c[1]
        nomemaior.append(c[0])
print(f'A quantidade de pessoas registradas foi de {contpessoas}')
print(f'O maior peso é de {maiorpeso}Kg. Peso de {nomemaior} ')
print(f'O menor peso é de {menorpeso}Kg. Peso de {nomemenor}')