## Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1- para binário; 2- para octal; 3- para hexadecimal

def main():

    num = int(input('Enter a number: '))

    binario = bin(num)
    octa = oct(num)
    hexa = hex(num)

    print(f"Binário: {binario}\nOctal: {octa}\nHexadecimal: {hexa}")

main()