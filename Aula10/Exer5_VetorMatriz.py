from random import seed
import random
seed(1)

lista = []

lista.append(random.randint(0, 10000))
lista.append(random.randint(0, 10000))
lista.append(random.randint(0, 10000))
lista.append(random.randint(0, 10000))

i = 4
j = 0
aux = 0

#a = input('Digite um numero: ')

for i in range(len(lista)):
    numero = i.split()
    junto = ''.join(numero)
    print(lista[i])
#if aux = lista[i]:
#    lista[i] = lista[j]
#    lista[j] = aux

#else:
#    print('Não é palíndromo')

# INCORRETO ATÉ O MOMENTO