## Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

maioridade: int = 0
quantidade: int = 7
ano = date.today().year

for c in range(1, quantidade + 1):
    nascimento = int(input(f"Informe o ano de nascimento da {c}º pessoa: "))
    if (ano - nascimento >= 18):
       maioridade += 1
print(f"{quantidade - maioridade} Ainda não atingiram a maioridade e {maioridade} já são maiores de idade")