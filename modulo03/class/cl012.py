## Dicionarios

pessoas = {
    'nome': 'Matheus',
    'sexo': 'M',
    'idade': 25
}
print(pessoas)
print(pessoas['nome'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)
for i in pessoas.items():
    print(f'Key: {i[0]} Value: {i[1]}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Fragata'
pessoas['peso'] = 80
print(pessoas)

## Dicionários dentro de uma lista
brasil = []
estado1 = {
    'UF': 'Rio de Janeiro',
    'Sigla': 'RJ'
}
estado2 = {
    'UF': 'São Paulo',
    'Sigla': 'SP'
}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['UF']) ## Rio de Janeiro
for estado in brasil:
    print(f'Estado: {estado["UF"]} - Sigla: {estado["Sigla"]}')
