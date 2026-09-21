## Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
##Ex: Ana Maria de Souza
## Primeiro = Ana
## Último = Souza

def main():
    name = input('Digite seu nome completo: ').strip()
    name_list = name.split()
    size = len(name_list)
    firstname = name_list[0].title()
    latname = name_list[size - 1].title()

    print(f"Primeiro nome: {firstname}, Último nome: {latname}")

main()