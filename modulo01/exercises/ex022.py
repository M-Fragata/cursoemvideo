## Crie um programa que leia o nome completo de uma pessoa e mostre:
## O nome com todas as letras maíusculas
## O nome com todas minúsculas
## Quantas letras ao todo (Sem considerar espaços)
## Quantas letras tem o primeiro nome

completeName = str(input('Digite seu nome completo: ')).strip()

print('Letras maiúsculas: {} /br Letras minúsculas: {} /br Characteres: {} /br Characteres primeiro nome: {}'.format(completeName.upper(), completeName.lower(), len(completeName), len(completeName.split()[0])))