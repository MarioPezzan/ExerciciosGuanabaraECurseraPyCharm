import random
from time import sleep
lista = list(range(61))
nsortidos = []
q = int(input('Quantos numeros vc quer que sorteia? '))
for c in range(q):
    nsortidos.clear()
    for n in range(6):
        aleatoria = random.choice(lista)
        nsortidos.append(aleatoria)
        lista.remove(aleatoria)
    lista = list(range(61))
    sleep(1.5)
    print(nsortidos)
