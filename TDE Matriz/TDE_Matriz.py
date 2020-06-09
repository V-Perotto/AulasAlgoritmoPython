from random import seed
import random
seed(1)


nLin = int(input('Digite o tamanho da Matriz NxN: '))
nCol = 5

matriz = [[]]

for nLin in range(nLin):
    matriz[nLin].append(random.randint(0, 1000))
    for nCol in range(nLin):
        matriz[nCol].append(random.randint(0, 1000))
print('-=' * 35)
for nLin in range(nLin):
    for nCol in range(nCol):
        print(f'[{matriz[nLin][nCol]:^5}]', end='')
    print()

# Solução inspirada a partir de outras soluções que vi nos comentários, em especial a do F. Rodrigues.

# A solução que cheguei com append em oito linhas:

#matriz = [[]]
#for nLin in range(3):
#    for nCol in range(3):
#        matriz[nLin].append(random.randint(0, 1000))
#print('-=' * 35)
#for nLin in range(3):
#    for nCol in range(3):
#        print(f'[{matriz[nLin][nCol]:^5}]', end='\n' if nCol == 2 else '')

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
# #