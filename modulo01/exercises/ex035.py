## Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
## regra, a soma de dois lados deve ser sempre maior que a medida do terceiro

def main():

    r1 = int(input('Primeiro valor: '))
    r2 = int(input('Segundo valor: '))
    r3 = int(input('Terceiro valor: '))

    status = True if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2 else False

    print(f"Pode ser formado um triângulo" if status else f"Não pode formar um triângulo")

main()