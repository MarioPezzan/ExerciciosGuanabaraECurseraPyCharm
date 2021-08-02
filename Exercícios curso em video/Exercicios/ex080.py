list = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        print('adicionado ao final da lista')
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'Valor adiconado na posição {pos} da lista')
                break
            pos += 1
print(list)



