## Faça um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado e a quantidade de dias pelas quais ela foi alugado. Calcule o preço a pagar. sabendo que o carro custa R$60.00 por dia e R$0.15 por KM rodado.

kilometers = float(input('Quantos Kilometros deseja converter? '))
days = int(input('Quantos dias de aluguel? '))

costDiary: int = 60 * days
costDistance: float = 0.15 * kilometers

print('com a quantidade de {}KM percorridos em {} dias o total a ser pago é de {}'.format(kilometers, days, costDiary + costDistance))

