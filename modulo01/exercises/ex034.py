## Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
## Para salários superiores a R$1.250,00 calcule um aumento de 10%
## para os inferiores ou iguais, o aumento é de 15%

def main():

    salary = float(input('Enter your salary: '))

    print(f"Aumento para: {salary * 0.1 + salary}" if salary > 1250 else f"Aumento para: {salary * 0.15 + salary}")

main()