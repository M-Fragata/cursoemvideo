## Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
## A) Quantos numeros foram digitados
## B) A lista de valores, ordenada de forma decrescente
## C) Se o valor 5 foi digitado e está ou não na lista

num_list = []

for c in range(1, 6):
    num = int(input(f'Informe o {c}º número: '))
    num_list.append(num)

print(f'Ao todo foram digitados {len(num_list)} números')
num_list.sort(reverse=True)
print(f'{num_list}')
if 5 in num_list:
    print(f'O valor 5 FOI digitado na {num_list.count(5)}º posição')
else:
    print(f'O valor 5 NÃO FOI digitado')