##Faça um programa que leia a largua e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

width = float(input('Digite a altura da parede em metros: '))
height = float(input('Digite a largura da parede em metros: '))

print('A área da parede é de {} metros e a quantidade de tinta necessária para pintá-la será de {} litros de tinta'.format(width * height, (width * height) / 2 ))