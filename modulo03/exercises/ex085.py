## Crie um programa aonde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num_list = [[],[]]

for c in range(1,8):
    num = int(input(f'informe o {c}º número: '))
    num_list[0].append(num) if num % 2 == 0 else num_list[1].append(num)

num_list[0].sort()
num_list[1].sort()

print(f'Lista de valores Pares: {num_list[0]}')
print(f'Lista de valores Impares: {num_list[1]}')