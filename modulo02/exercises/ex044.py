## Elabore um programa que calcule o valor a ser pago por um produto. Considerando o seu preço normal e condição de pagamento:
## à vista dinheiro/cheque: 10% de desconto
## à vista no cartão: 5% de desconto
## em até 2x no cartão: preço normal
## 3x ou mais no cartão: 20% de juros

def main():
    print(f"========== Fragata's Store ==========")
    value = float(input("Digite o valor do produto: "))

    pagamento = int(input(f"Formas de pagamento: \n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\nQual é a opção?"))

    if pagamento == 1:
        payment = value - value * 0.1
        print(f"desconto de R${value * 0.1:.2f}, total de R${payment:.2f}")
    elif pagamento == 2:
        payment = value - value * 0.05
        print(f"desconto de R${value * 0.05:.2f}, total de R${payment:.2f}")
    elif pagamento == 3:
        payment = value
        print(f"2x de {payment / 2:.2f}, total de R${payment:.2f}")
    elif pagamento == 4:
        payment = value + value * 0.2
        print(f"3x de {payment / 3:.2f} com JUROS, total de R${payment:.2f}")
    else:
        print('Forma de pagamento não encontrada')

main()