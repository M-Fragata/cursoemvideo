## Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}
gols = []
dados['nome'] = input('Qual nome do jogador? ').title().strip()
partidas = int(input('Quantas partidas foram jogadas? '))

for c in range(1, partidas + 1):
    gol = int(input(f'Quantos gols na {c}º partida: '))
    gols.append(gol)
dados['gols'] = gols

dados['total'] = sum(dados['gols'])

print('-='*20)
print(dados)
print('-='*20)
print(f'O campo nome tem o valor {dados["nome"]}')
print(f'O campo gols tem o valor {dados["gols"]}')
print(f'O campo total tem o valor {dados["total"]}')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for c in range(1, len(dados['gols']) + 1):
    print(f'    => Na {c}º partida, fez: {dados["gols"][c-1]}')
print(f'Foi um total de {dados["total"]} gols.')