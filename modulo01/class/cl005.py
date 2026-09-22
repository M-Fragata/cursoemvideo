## condicionais

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')

## Exemplos práticos
print('Exemplo 1')
nome = str(input('Qual o seu nome? '))

if nome.title() == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Que nome normal!')
print(f"Bom dia, {nome}!")

print('Exemplo 2')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f"A sua média foi de {media:.1f}")
print('Aprovado' if media >= 7 else 'Reprovado')