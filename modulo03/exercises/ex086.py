## Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        position = int(input((f'Informe o número da posição [{i},{j}]: ')))
        matriz[i].append(position)


for c in range(0,3):
    num = matriz[c]
    for n in range(0,3):
        print(f'[ {num[n]} ]', end=" ")
    print()