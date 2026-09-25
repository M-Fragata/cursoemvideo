## Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s: int = 0
for c in range(1, 500, 2):
    s += c
print(f"A soma total dos números negativos entre 1 e 500 é de {s}")