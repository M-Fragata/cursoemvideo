## crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

resultado = {}
for c in range(1, 5):
    resultado[f'jogador{c}'] = randint(1,6)
    print(f'O jogador{c} tirou {resultado[f"jogador{c}"]} pontos')
    sleep(1)

ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)

contador = 0
print('Ranking dos jogadores: ')
for jogo in ranking:
    print(f'    {contador + 1}º lugar: {f"{ranking[contador][0]}"} com {ranking[contador][1]} pontos')
    contador += 1
    sleep(1)