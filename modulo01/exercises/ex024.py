## Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

def main():
    city = str(input('Informe o nome de uma cidade: ')).strip()

    citystart = 'inicia' if city.upper().startswith('SANTO') else 'não inicia'

    print(f"A cidade {city.upper()} {citystart} com 'SANTO'")

main()