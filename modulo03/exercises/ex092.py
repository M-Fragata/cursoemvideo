## Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
## considere aposentadoria 35 anos de trabalho
from datetime import date

now = date.today().year

dados = {}


dados['nome'] = input('Nome: ').title().strip()
dados['idade'] = now - int(input('Ano de nascimento: '))
dados['carteira'] = int(input('Cateira de trabalho [0 não tem]: '))
if dados['carteira'] != 0:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$'))


print(dados)
print(f'Nome tem o valor {dados["nome"]}')
print(f'idade tem o valor {dados["idade"]}')
print(f'ctps tem o valor {dados["carteira"]}')
if dados['carteira'] != 0:
    print(f'contratação tem o valor {dados["contrato"]}')
    print(f'Salário tem o valor de R${dados["salario"]}')
    print(f'aposentadoria tem o valor de {35 + dados["contrato"] - dados["idade"]}')
