## Escreva um programa que leia a velocidade de um carro.
## Se ele ultrapasar 80km/h, mostre uma mensagem dizendo que ele foi multado.
## A multa vai custar R$7,00 por cada km acima do limite.

def main():

    car_speed = float(input('Enter the car speed: '))

    if(car_speed < 0 ):
        print('The car speed is too low')
        return

    multado = car_speed > 80
    velocidadeacima = car_speed - 80
    print(f"{velocidadeacima}Km/h acima da velocidade máxima, multa de: {velocidadeacima * 7}" if multado else f"Velocidade OK")

main()