## Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
## anos bissextos são divisiveis por 4 e se terminarem em 00 divisiveis por 400

def main():
    year = int(input('Informe um ano: '))

    print('Ano Bissexto' if year % 4 == 0 or year % 400 == 0 else 'Ano Não bissexto')

main()