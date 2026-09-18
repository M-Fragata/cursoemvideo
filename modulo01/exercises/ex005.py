##Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

n1 = int(input('Enter a number: '))

def main(number):
    print('Número anterior: {} \n Número posterior: {}'.format(number-1, number+1))

main(n1)