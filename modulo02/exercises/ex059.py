## Crie um programa que leia dois valores e mostre um menu na tela:
## [ 1 ] somar
## [ 2 ] multiplicar
## [ 3 ] maior
## [ 4 ] novos números
## [ 5 ] sair do programa
## Seu programa deverá realizar a operação solicitada em cada caso.

action = 0

while action != 5:
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))

    print('Selecione um comando abaixo')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    action = int(input('Informe qual ação deseja realizar: '))

    if action == 1:
        print(f"A soma de {n1} com {n2} é de {n1 + n2}.")
    elif action == 2:
        print(f"A multiplicação de {n1} com {n2} é de {n1 * n2}.")
    elif action == 3:
        print(f"O número {n1} é maior do que o {n2}" if n1 > n2 else f"O número {n2} é maior do que o {n1}.")
    elif action == 5:
        print(f"Usuário sendo desligado do programa!")
    