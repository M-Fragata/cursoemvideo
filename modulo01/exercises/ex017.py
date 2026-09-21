##Faça um programa que leita o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo. calcule e mostre o comprimento da hipotenusa

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))

def calculoHipotenusa(catetooposto:float, catetoAdjacente: float):
    result = ((catetooposto**2) + (catetoAdjacente**2))**(1/2)
    return result

print('A hipotenusa é {:.2f}'.format(calculoHipotenusa(catetoOposto, catetoAdjacente)))