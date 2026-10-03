## Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    print("-="*20)
    m = num[0]
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5)
        if n > m:
            m = n
    print(f"Foram informados {len(num)} números")
    print(f"O maior número foi {m}")

maior(1,2,3,4,5,6,7,8,9,10)