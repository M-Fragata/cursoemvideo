## Aprimore o desafio anterior, mostrando no final:
## A) A soma de todos os valores pares digitados
## B) A soma de todos os valores ímpares digitados
## C) O maior valor da segunda linha.

matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        position = int(input((f'Informe o número da posição [{i},{j}]: ')))
        matriz[i].append(position)

soma_par = 0
soma_impar = 0
maior = max(matriz[1])

for c in range(0,3):
    num = matriz[c]
    for n in range(0,3):
        print(f'[ {num[n]} ]', end=" ")
        if num[n] % 2 == 0:
            soma_par += num[n] 
        else:
            soma_impar += num[n]
    print()

print(f"A soma dos valores Pares: {soma_par}\nA soma dos valores Impares: {soma_impar}\nO maior valor da segunda linha: {maior}")

