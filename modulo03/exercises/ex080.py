## Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

num_list = []

for c in range(1, 6):
    num = int(input(f'Informe o {c}º número: '))
    if c == 1 or num >= num_list[-1]:
        num_list.append(num)
        print('Adicionado ao final da lista...')
    else:
        for index, n in enumerate(num_list):
            if num <= n:
                num_list.insert(index,num)
                print(f'Adicionando na posição {index} da lista...')
                break

print(f'Os valores digitados em ordem foram: {num_list}')
     
