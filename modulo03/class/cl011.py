# listas dentro das listas
pessoas = []

dados = []
dados.append('Pedro')
dados.append(25)

pessoas.append(dados[:])
print(pessoas[0][0])

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[3][1])
for p in galera:
    print(p[0], end=' ')
    print(p[1])

pessoal = []
temporario = []
for c in range(0,3):
    temporario.append(input('Nome: ').title().strip())
    temporario.append(int(input('idade: ')))
    pessoal.append(temporario[:])
    temporario.clear()
print(temporario)
print(pessoal)

for p in pessoal:
    if p[1] >= 30:
        print(f'{p[0]}')
    else:
        print(f'{p[0]}')
