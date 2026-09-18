##Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuáda;

number = int(input('Enter a number: '))

def main(n: int):
    counter = 0
    while counter <= 10:
        print('{} x {} = {}'.format(n, counter, n * counter))
        counter += 1

main(number)