## Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

palpite = int(input('Quantos palpites deseja criar? '))

palpites = []
dados = []

for c in range(1, palpite + 1):
    while len(palpites) < 6:
        pal = randint(1,60)
        if not pal in dados:
            dados.append(pal)
        if len(dados) >= 6:
            dados.sort()
            palpites.append(dados[:])
            dados.clear()
            break

for p in palpites:
    print(p)
    sleep(1)