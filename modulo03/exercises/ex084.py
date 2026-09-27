## Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
## A) Quantas pessoas foram cadastradas
## B) Uma listagem com as pessoas mais pesadas 
## C) Uma listagem com as pessoas mais leves 

pessoas = []
dados = []

while True:

    dados.append(input('Nome: ').title().title())
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    status = input('Deseja parar? [S/N]: ').strip().upper()
    if status == 'S':
        break

tot = len(pessoas)
pesadas = []
leves = []

for i, p in enumerate(pessoas):

    if i == 0 or p[1] <= leves[0][1]:
        if len(leves) > 0 and p[1] < leves[0][1]:
            leves.pop()
        leves.append(p)

    if i == 0 or p[1] >= pesadas[0][1]:
        if len(pesadas) > 0 and p[1] > pesadas[0][1]:
            pesadas.pop()
        pesadas.append(p)
        
print(f'{len(pessoas)} pessoa(s) foram cadastrada(s) ao todo')
print(f'Lista de pessoas mais pesadas: {pesadas}')
print(f'Lista de pessoas mais leves: {leves}')
