## Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
## Equilátero: Todos os lados iguais
## Isósceles: dois lados iguais
## Escaleno: Todos os lados diferentes

def main():

    tri1 = int(input('Lado 1 do triângulo: '))
    tri2 = int(input('Lado 2 do triângulo: '))
    tri3 = int(input('Lado 3 do triângulo: '))

    is_triangle = True if tri1 + tri2 > tri3 and tri2 + tri3 > tri1 and tri1 + tri3 > tri2 else False
    if is_triangle == False:
        print(f"Valores não formam um triângulo!")
        return

    print('Triângulo Equilátero' if tri1 == tri2 == tri3 else f"Triângulo Escaleno" if tri1 != tri2 != tri3 else f"Triângulo Isósceles")

main()