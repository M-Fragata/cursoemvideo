## Crie uma tupla preenchida com os 20 primeiros colocaros da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
## a) Apenas os 5 primeiros colocados.
## b) Os últimos 4 colocados.
## c) Uma lista com os times em ordem alfabética.
## d) Em que posição está o time da Chapecoense.

brasileirao = (
    "Flamengo",
    "Palmeiras",
    "Athletico-PR",
    "Fluminense",
    "Bahia",
    "Cruzeiro",
    "Atlético-MG",
    "Santos",
    "Coritiba",
    "Red Bull Bragantino",
    "São Paulo",
    "Botafogo",
    "Vitória",
    "Corinthians",
    "Mirassol",
    "Vasco da Gama",
    "Grêmio",
    "Internacional",
    "Remo",
    "Chapecoense"
)

for i, time in enumerate(brasileirao):
    if time == 'Chapecoense':
        index = i + 1

print(f'5 primeiros colocados são: {brasileirao[:5]}')
print(f'últimos 4 colocados são: {brasileirao[-4:]}')
print(f'Lista dos times em ordem alfabética: {sorted(brasileirao)}')
print(f'Chapecoense está em {index}º lugar')