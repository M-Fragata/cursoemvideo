## Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(name='Desconhecido', goals=0):
    if name == '':
        name = '<desconhecido>'
    print(f"O jogador {name} fez {goals} gol(s) no campeonato.")

nome = input('Nome do jogador? ').title().strip()
gols = int(input('Número de gols: '))
ficha(nome, gols)