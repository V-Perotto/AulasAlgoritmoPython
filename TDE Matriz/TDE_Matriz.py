from random import seed
import random
seed(1)

nLin = int(input('Digite o tamanho da Matriz [N, N]: '))
cont = nLin
matriz = []

for lin in range(nLin):
    linha = []
    for col in range(nLin):
        linha.append(random.randint(0, 1000))
    matriz.append(linha)

while cont > 0:
    cont = cont - 1
    print(matriz[cont])

m = int(input('Selecione a quantidade de casas para percorrer: '))
points = 0

for pos_i in range(nLin):
    for pos_j in range(nLin):
        for i in range(pos_i, m + 1, -1):
            points = points + matriz[pos_i][i]
        for j in range(pos_i, m + 1, +1):
            points = points = matriz[pos_i][j]
print(points)