## Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas b) A média de idade c) Uma lista com as mulheres d) Uma lista com as pessoas com idade acima da média

dados = []

while True:
    dado = {}
    dado['nome'] = input('Nome: ').title().strip()
    dado['sexo'] = input('Sexo: [F/M] ').upper().strip()
    dado['idade'] = int(input('Idade: '))
    dados.append(dado)

    status = input('Deseja continuar? [S/N] ').upper().strip()
    if status == 'N':
        break

media = sum(d['idade'] for d in dados) / len(dados)
quantidade_pessoas = len(dados)
mulher = []
acima_media = []

for d in dados:
    if d['sexo'] == 'F':
        mulher.append(d['nome'][:])
    if d['idade'] > media:
        acima_media.append(d)
print('-='*20)
print(f'O grupo tem {quantidade_pessoas} pessoas')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: {mulher}')
print(f'Lista das pessoas que estão acima da média: ')
for c in acima_media:
    print(f'Nome = {c["nome"]}', end=', ')
    print(f'Sexo = {c["sexo"]}', end=', ')
    print(f'Idade = {c["idade"]}')
    print()
