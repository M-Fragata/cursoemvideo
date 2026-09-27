## Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletim = {}

name = input("Digite o nome do aluno: ").title().strip()
media = float(input('Digite a média do aluno: '))

boletim['nome'] = name
boletim['media'] = media
boletim['status'] = 'Aprovado' if media >= 7 else 'Reprovado'

print(f'Nome é igual a {boletim["nome"]}.\nMédia é igual a {boletim["media"]}.\nSituação é igual a {boletim["status"]}!')