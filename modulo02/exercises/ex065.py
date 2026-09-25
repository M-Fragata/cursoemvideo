## Faça um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

status = True

tot = 0
counter = 0
maior = 0
menor = 0

while status:

    num = int(input('Informe um número inteiro: '))

    tot += num
    counter += 1

    if counter == 1:
        maior = num
        menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    print('=-='* 10)
    print('Ações disponíveis: ')
    print('[ 1 ] - Continuar ')
    print('[ 2 ] - Parar ')
    action = int(input('Informe a ação desejada: '))
    print('=-='* 10)

    if action == 2:
        print(f"Média total: {tot/counter:.1f}\nMaior valor: {maior}\n Menor valor: {menor}")
        break

