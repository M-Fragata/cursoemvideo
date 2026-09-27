## Aprimore o desafio 093 "## Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."
# para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []

while True:
    print('='*20)
    dados = {}
    dados['nome'] = input('Nome do jogador? ').upper().title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols_list = []
    for c in range(1, partidas+1):
        partida = int(input(f'Gols na {c}º partida: '))
        gols_list.append(partida)
    dados['gols'] = gols_list
    jogadores.append(dados.copy())
    status = input('Deseja continuar? [S/N] ').upper().strip()
    if status == 'N':
        break
print('-='*20)
print(f' Cod nome            gols          total')
print('-'*40)


for i, jogador in enumerate(jogadores):
    print(f"{i:>3} {jogador['nome']:<15} {str(jogador['gols']):<15} {sum(jogador['gols'])} ")

while True:
    print('-'*40)
    contador = 1
    dados_jogador = int(input('Mostrar dados de qual jogador? [999 parar]'))
    if dados_jogador == 999:
        break

    if dados_jogador >= len(jogadores):
        print(f'Codigo inválido')
    else:
        jogador = jogadores[dados_jogador]
        print(f"Levantamento do jogador {jogador['nome']}:")
            
        for i, gol in enumerate(jogador['gols']):
            print(f"    No jogo {i+1} fez {gol} gols.")
