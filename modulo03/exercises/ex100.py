## Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint



def sorteia(lista):
    for c in range(1,6):
        lista.append(randint(1,100))

def somapar(numeros):
    pares = sum(n for n in numeros if n%2==0)
    count = sum(1 for n in numeros if n%2==0)
    print(f"A lista {numeros} possui um total de {count} números pares que a soma vale {pares}.")

numeros = []
sorteia(numeros)
somapar(numeros)