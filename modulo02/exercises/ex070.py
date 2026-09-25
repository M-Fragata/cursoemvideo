## Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
## A) qual é o total gasto na compra.
## B) quantos produtos custam mais de R$1000.
## C) qual é o nome do produto mais barato.

tot = prod_price = 0
prod_name = ''
expensiver = 0

while True:
    product = input('Informe o nome do produto: ').strip().title()
    price = float(input('Informe o preço do produto: R$ '))
    status = input('Continuar compras? [S/N]: ').upper().strip()

    tot += price
    if price > 1000:
        prod_price += 1
    if price > expensiver:
        expensiver = price
        prod_name = product

    if status == 'N':
        print('Fechando carrinho...')
        break

print(f'R${tot} gastos na compra.\n{prod_price} produto(s) acima de R$1000,00.\n{prod_name} foi o produto mais caro.')