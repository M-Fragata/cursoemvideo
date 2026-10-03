## Funções

def cabecalho(content):
    t = len(content) + 6
    print("-" * t)
    print(f"   {content}   ")
    print("-" * t)

cabecalho("Hello World!")

print('//////////////')

def soma(a: int, b: int):
    return a + b
s = soma(2,5)
print(s)

print('//////////////')

def contador(*num): ## *num aceita vários parâmetros numericos e vira uma TUPLA
    print(len(num))
    for n in num:
        print(n, end=" -> ")
    print('Fim')
contador(1,2,3,4,5,6,7)


def dobra(v):
    c = 0
    while c < len(v):
        v[c]*=2
        c+=1

valores = [10,20,30,40,50,60,70,80,90,100]
dobra(valores)
print(valores)