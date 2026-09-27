## crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep

resultado = []
for c in range(1, 5):
    dado = {
        'jogador':f'jogador{c}',
        'jogada': randint(1,6)
        }
    resultado.append(dado.copy())
    print(f'O jogador{c} tirou {dado["jogada"]} pontos')
    sleep(1)
    dado.clear()

for c in range(0,4):
    for i, jogo in enumerate(resultado):

        if i < len(resultado) -1:
            if resultado[i]['jogada'] < resultado[i+1]['jogada']:
                resultado[i]['jogada'], resultado[i+1]['jogada'] = resultado[i+1]['jogada'], resultado[i]['jogada']
                resultado[i]['jogador'], resultado[i+1]['jogador'] = resultado[i+1]['jogador'], resultado[i]['jogador']
                ## aqui poderia ter simplesmente feito: resultado[i], resultado[i+1] = resultado[i+1], resultado[i]

contador = 1
print('Ranking dos jogadores: ')
for jogo in resultado:
    print(f'    {contador}º lugar: {jogo["jogador"]} com {jogo["jogada"]} pontos')
    contador += 1
    sleep(1)