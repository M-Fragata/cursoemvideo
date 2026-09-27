## Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = []

while True:
    name = input('Informe o nome do aluno: ')
    n1 = float(input('Digite a 1º nota: '))
    n2 = float(input('Digite a 2º nota: '))
    boletim.append([name,[n1, n2]])

    status = input('Deseja cadastrar mais alguém? [S/N]').upper().strip()
    if status == 'N':
        break

print('=-='*10)
print('Quadro de boletim')
print('=-='*10)
print('Nº   Nome          Média')
for i, b in enumerate(boletim):
    med = (b[1][0] + b[1][1]) / 2
    print(f'{i:<4} {b[0]:<10} {med:>8.1f}')
print('=-='*10)
while True:
    num = int(input('Informe o Nº que deseja saber as notas: [999 para sair]'))
    if num == 999:
        print('Saindo do boletim')
        break
    print(f'Notas: {boletim[num][1]}')