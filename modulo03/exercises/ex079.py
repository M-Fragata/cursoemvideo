## Crie um programa onde o usuário possa digitar varios valores numericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num_list = []

while True:
    num = int(input('Informe um número: '))

    if num in num_list:
        print('Número já cadastrado!')
    else:
        print('Cadastrando número!')
        num_list.append(num)

    status = input('Deseja continuar? [S/N]').upper().strip()
    if status == 'N':
        print('Parando cadastro de números!')
        break


num_list.sort()

print(f'Valores únicos digitados em ordem crescente: {num_list}')