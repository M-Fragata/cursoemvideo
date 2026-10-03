def aumentar(n, format=False):
    if format == True:
        return real(n*0.10 + n)
    return n*0.10 + n
def diminuir(n, format=False):
    if format == True:
        return real(n - n*0.13)
    return n - n*0.13
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