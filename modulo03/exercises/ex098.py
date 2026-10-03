## Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
## a) De 1 até 10, de 1 em 1
## b) De 10 até 0, de 2 em 2
## c) Uma contagem personalizada

from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    print("-="*21)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i > f:
        for c in range(i, f - 1, -p if p > 0 else p):
            print(c, end=' ')
        print("Fim!")
        
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ')
        print("Fim!")
    sleep(1)


contador(1,10,1)
contador(10, 0, -2)

print(f"Agora é sua vez de personalizar a contagem!")
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)