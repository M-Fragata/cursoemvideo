## Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Enter a number: '))

contador = 0
for c in range(1, num+1):
    if num%c == 0:
        contador += 1

print(f"O número {num} NÃO É um número primo!!" if (contador >= 3) else f"O número {num} É um número primo!!")