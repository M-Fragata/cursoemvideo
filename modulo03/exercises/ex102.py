## Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(fat, show=False):
    s = 1
    for c in range(1, fat):
        if show == True:
            print(f"{s}", end=' ')
        s*= (c+1)
    print('=',s)

fatorial(10, True)