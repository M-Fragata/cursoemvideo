## Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitar for ímpar desconsidere-o.

s = 0

for c in range(1, 7):
    n = int(input(f"Informe o {c}º número: "))
    s += n if n%2 == 0 else ''
print(f"O somatório dos números pares foi de: {s}")
