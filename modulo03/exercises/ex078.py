## Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num_list = []

for c in range(1, 6):
    num = int(input(f'Informe o {c}º número: '))
    num_list.append(num)

maior = 0
index_maior = 0
menor = 0
index_menor = 0

for index, num in enumerate(num_list):
    if index == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
        index_maior = index
    if num < menor:
        menor = num
        index_menor = index

print(f'Lista: {num_list}\nMaior: {maior}, Posição: {index_maior + 1}º, Index: {index_maior}\nMenor: {menor}, Posição: {index_menor + 1}º, Index: {index_menor}')