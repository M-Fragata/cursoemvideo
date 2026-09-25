## Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input(f"Informe um número: "))

fatorial = num
counter1 = num

while counter1 > 1:
    print(f"{fatorial} x {(counter1 - 1)}")
    fatorial = fatorial * (counter1 - 1)
    counter1 -= 1

print(f"O fatorial de {num} é {fatorial}")

