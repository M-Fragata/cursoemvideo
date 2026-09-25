## Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0.0
menor = 0.0

for c in range(1,6):
    peso = float(input(f"Informe o peso da {c}º pessoa: "))
    if peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso

print(f"Maior peso: {maior:.2f}\nMenor peso: {menor:.2f}")
