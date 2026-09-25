## Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

contador = 1

while contador <= 10:
    print(f"{contador}º termo: {termo}")
    contador += 1
    termo = termo + razao