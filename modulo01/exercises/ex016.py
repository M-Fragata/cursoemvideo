##Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc

n1 = float(input('Enter a number: '))
print('o valor digitado foi {} e a sua porção inteira é de {}'.format(n1, trunc(n1)))