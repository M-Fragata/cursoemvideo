## Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

def main():
    number = int(input('Enter a number: '))
    print('Par' if number % 2 == 0 else 'Impar')

main()
