## Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

def main():

    n1 = int(input('Enter a number: '))
    n3 = int(input('Enter another number: '))
    n2 = int(input('Enter another number: '))

    bigger = 0
    smallest = 0

    if n1 > n2 and n1 > n3:
        bigger = n1
        smallest = n2 if n2 < n3 else n3
    if n2 > n1 and n2 > n3:
        bigger = n2
        smallest = n1 if n1 < n3 else n3
    if n3 > n2 and n3 > n1:
        bigger = n3
        smallest = n2 if n2 < n1 else n1

    print(f"Maior: {bigger}, Menor: {smallest}")

main()