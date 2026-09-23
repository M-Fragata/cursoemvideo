## Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem: - O primeiro valor é maior; O segundo valor é maior; Não existe valor maior, os dois são iguais.

def main():

    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    print(f"{num1} é maior do que {num2}" if num1 > num2 else f"{num2} é maior do que {num1}" if num2 > num1 else "Os dois valores são iguais")

main()