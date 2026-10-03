def aumentar(n, discount,format=False):
    if format == True:
        return real(n*(discount/100) + n)
    return n*(discount/100) + n

def diminuir(n, discount, format=False):
    if format == True:
        return real(n - n*(discount/100))
    return n - n*(discount/100)

def dobro(n, format=False):
    if format == True:
        return real(n*2)
    return n*2

def metade(n, format=False):
    if format == True:
        return real(n/2)
    return n/2

def real(n):
    r = f"{n:.2f}"
    return f"R${str(r)}"

def resumo(n, aumento, reducao):
    print('='*25)
    print("RESUMO DO VALOR")
    print('='*25)
    print(f"Preço analisado: {real(n)}")
    print(f"Dobro do preço: {dobro(n, True)}")
    print(f"Metade do preço: {metade(n, True)}")
    print(f"{aumento}% de aumento: {aumentar(n, aumento, True)}")
    print(f"{reducao}% de aumento: {diminuir(n, reducao, True)}")
    print("="*25)