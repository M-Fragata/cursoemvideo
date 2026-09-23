## Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar; - se é a hora de se alistar; - se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo

def main():

    age = int(input('whats your age? '))

    print(f"Deve se alistar ao exército! prazo vencido de {age - 18} anos" if age > 18 else f"Está na hora de se alistar!" if age == 18 else f"Ainda não possui idade para se alistar, prazo de {18 - age} anos")

main()