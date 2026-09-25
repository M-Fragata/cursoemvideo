## Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

final = termo + razao * 10

for c in range (termo, final, razao):
    print(c)