##Faça um programa que leia um angulo qualquer e mostre na sua tela o valor do seno, cosseno e tangenta desse ângulo.
import math

angle = float(input('Digite um ângulo: '))

def main():
    print('Seno: {}'.format(math.sin(math.radians(angle))))
    print('Coseno: {}'.format(math.cos(math.radians(angle))))
    print('Tangente: {}'.format(math.tan(math.radians(angle))))

main()