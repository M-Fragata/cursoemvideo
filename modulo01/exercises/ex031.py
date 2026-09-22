## Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas.

def main():
    distance = float(input('Enter de distance in Km: '))

    if(distance <= 0):
        print('Distancia invalida')
        return

    print(f"Price: {distance * 0.5 + distance}Km" if distance <= 200 else f"price: {distance * 0.45 + distance}Km")

main()