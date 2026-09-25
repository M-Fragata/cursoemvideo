## Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
## A) quantas pessoas tem mais de 18 anos.
## B) quantos homens foram cadastrados.
## C) quantas mulheres tem menos de 20 anos.

older_18 = 0
women_younger_20 = 0
mens = 0 

while True:
    print('=-=' * 12)
    print('Cadastro de pessoas no banco de dados')
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo [M]/[F]: ').upper().strip()
    print('=-=' * 10)
    status = input('Deseja continuar? [S]/[N]: ').upper().strip()

    if idade > 18:
        older_18 += 1
    if idade < 20 and sexo == 'F':
        women_younger_20 += 1
    if sexo == 'M':
        mens += 1

    if status == 'N':
        print('Fechando cadastro!')
        break
print('Dados cadastrados: ')
print(f'{older_18} pessoa(s) maior(es) de 18 anos\n{mens} homem(ns)\n{women_younger_20} mulher(es) com idade(s) abaixo de 20 anos')
