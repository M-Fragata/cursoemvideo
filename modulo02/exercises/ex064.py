## Faça um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = 0
counter = 0
sum = 0

while num != 999:
    num = int(input(f"Caso deseje parar o programa apenas digite o número '999'\nInforme um número: "))
    if num != 999:
        sum += num
        counter += 1
print(f"Ao todo foram digitados {counter} números com somatória total de {sum}.")