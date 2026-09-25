## Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo;
# Qual é o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos.

data = []

quantidade = 4

for c in range (1, quantidade + 1):
    print(f"Informações da {c}º pessoa:")
    idade = int(input(f"Informe a idade: "))
    nome = str(input('Informe o nome: ')).strip().upper()
    sexo = str(input(f"Informe seu sexo\n'M' para masculino e 'F' para feminino: ")).strip().upper()

    if sexo not in ['M', 'F']:
        print('Sexo inválido!')
        break

    data.append([nome, idade, sexo])

tot_age = 0
older_man_name = ''
older_man_age = 0
women_younger_than_20 = 0

for c in range(0, quantidade):
    user = data[c]
    [nome, idade, sexo] = user

    tot_age += idade

    if sexo == 'F' and idade < 20:
        women_younger_than_20 += 1

    if sexo == 'M' and idade > older_man_age:
        older_man_name = nome
        older_man_age = idade

print(f"A média de idade do grupo é de: {tot_age/quantidade} anos\nO nome do homem mais velho é o: {older_man_name}\nO grupo possui {women_younger_than_20} mulher(es) com menos de 20 anos")