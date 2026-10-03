## Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        print('ERRO! Digite um número inteiro válido')
    return int(num)

n = leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número {n}")