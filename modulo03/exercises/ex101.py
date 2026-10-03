## Crie um programa que tenha um função chamada voto() que receba como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date

     
y = date.today().year
nascimento = int(input('Em que ano você nasceu? '))

def voto(ano: int):
    idade = y - nascimento
    if idade < 16:
        return [idade, 'NEGADO']
    if idade >= 16 and idade < 18 or idade >=65:
        return [idade, 'OPCIONAL']
    if idade >= 18:
        return [idade, 'OBRIGATÓRIO']

resultado = voto(nascimento)

print(f"Com {resultado[0]} anos: {resultado[1]}")
