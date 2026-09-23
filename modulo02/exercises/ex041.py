## A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
## Até 9 anos: MIRIM
## Até 14 anos: INFANTIL
## Até 19 anos: JUNIOR
## Até 20 anos: SENIOR
## Acima: MASTER
from datetime import date


def main():

    year = int(input('what year were you born? '))

    nascimento = date.today().year - year

    print(f"Categoria MIRIM" if nascimento <= 9 else f"Categoria INFANTIL" if nascimento > 9 and nascimento <= 14 else f"Categoria JUNIOR" if nascimento > 14 and nascimento <= 19 else f"Categoria SENIOR" if nascimento == 20 else f"Categoria MASTER")

main()