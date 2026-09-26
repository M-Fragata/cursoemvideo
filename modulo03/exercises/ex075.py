## Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
## A) Quantas vezes apareceu o valor 9.
## B) Em que posição foi digitado o primeiro valor 3.
## C) Quais foram os números pares.

numeros = (
        int(input(f'informe o 1º número: ')),
        int(input(f'informe o 2º número: ')),
        int(input(f'informe o 3º número: ')),
        int(input(f'informe o 4º número: '))
        )


print('Lista: ',numeros)
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O primeiro valor número 3 foi digitado em {numeros.index(3) + 1}º lugar')
else:
    print(f'Não foi informado nenhum número "3"')

print(f'Números pares: ', end='')
par = False
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
        par = True
if not par:
    print('Nenhum número par foi digitado.')
