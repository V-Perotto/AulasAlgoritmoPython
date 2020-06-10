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
        #calculo = calcularPontuacaoPosicao()
        #for nCol in range(0, matriz, 1):
        #    for cima in range(0, m):
        #        pos_cima = cima
        #for nCol in range(0, matriz, -1):
        #   for baixo in range(0, m):
        #        pos_baixo = baixo
        #for nLin in range(0, matriz, -1):
        #    for esquerda in range(0, m):
        #        pos_esquerda = esquerda
        #for nLin in range(0, matriz, 1):
        #    for direita in range(0, m):
        #        pos_direita = direita
    matriz.append(linha)

while cont > 0:
    cont = cont - 1
    print(matriz[cont])

# percorrer matriz
# for das linhas
#     for das colunas
#          calcular pontuacao da posicao
#          for pra ir pra esquerda
#               somar pontuacao
#          for pra ir pra direita
#               somar pontuacao
#          for pra ir pra baixo
#               somar pontuacao
#          for pra ir pra cima
#               somar pontuacao
#          verifica se a pontuacao eh maior que a maior pontuacao
#               atualiza a posicao da maior pontuacao
# # #