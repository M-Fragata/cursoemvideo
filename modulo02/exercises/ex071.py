## Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
## OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

value = int(input('Informe valor a ser sacado: '))

n50 = value // 50
value = value%50

n20 = value // 20
value = value%20

n10 = value // 10
value = value%10

n01 = value // 1
value = value%1

print(f'Foram utilizadas as seguintes quantidades de notas:\n{n50} notas de R$ 50\n{n20} notas de R$ 20\n{n10} notas de R$ 10\n{n01} notas de R$ 1')