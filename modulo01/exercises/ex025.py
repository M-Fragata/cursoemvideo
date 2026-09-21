## Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

def main():

    nome = input('Whats your name? ').strip()

    status = 'possui' if nome.upper().find('SILVA') != -1 else 'não possui'

    print(f"{nome.title()} {status} 'SILVA' no nome")

main()