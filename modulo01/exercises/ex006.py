##Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Enter a number: '))

def main(number: int):
    print('The double is: {}'.format(number*2))
    print('The triple is: {}'.format(number*3))
    print('The square is: {}'.format(number**(1/2)))

main(n1)