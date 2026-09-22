## Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


def main():

    house_price = float(input('Qual o valor do imóvel? '))
    salary = float(input('Qual é o seu salário? '))
    time = float(input('Irá quitar o imóvel em quantos anos? '))

    prestacao = house_price / (time * 12) ## passando de ano para mês

    status = prestacao < salary

    print(f"Empréstimo liberado com mensalidade de R${house_price / 12} durante {time} anos" if status else f"Empréstimo negado, pois a mensalidade de R${prestacao} excede o salário de R${salary}")

main()