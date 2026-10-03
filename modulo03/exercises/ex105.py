## Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
## - Quantidade de notas
## - A maior nota
## - A menor nota
## - A média da turma
## - A situação (opcional)
## Adicione também as docstrings da função.

def notas(*num):
    m = sum(num)/len(num)
    dados = {
        'total': len(num),
        'maior': max(num),
        'menor': min(num),
        'media': m,
        'situacao': 'Boa' if m >= 7.0 else 'Ruim'
    }
    return dados
    

response = notas(5.5, 9.5, 10, 6.5)
print(response)
