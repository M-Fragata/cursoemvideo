##Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere us$1.00 = R$3.27

howMuchBrazilianMoneyDoYouHave = float(input('How much money do you have? '))

def main():
    print('With R${:.2f} you can convert US${:.2f}'.format(howMuchBrazilianMoneyDoYouHave, howMuchBrazilianMoneyDoYouHave / 3.27))

main()
