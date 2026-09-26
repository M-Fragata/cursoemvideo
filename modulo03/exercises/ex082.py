## Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

num_list = []

while True:

    num = int(input('Digite um número: '))
    num_list.append(num)

    status = input('Deseja continuar? [S/N]: ').upper().strip()
    if status == 'N':
        break

par_list = []
impar_list = []

for num in num_list:
    if num%2==0:
        par_list.append(num)
    else:
        impar_list.append(num)
print(f'Lista Total: {num_list}\nLista Par: {par_list}\nLista Impar: {impar_list}')