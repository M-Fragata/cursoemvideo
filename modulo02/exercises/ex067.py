## Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    print('=-=' * 10)
    num = int(input('quer ver a tabuada de qual valor? '))
    if num < 0:
        print('Programa desligado devido ao usuário ter digitado valor negativo')
        break
    print('=-=' * 10)
    print('--Tabuada--')
    for c in range(0, 10):
        print(f'{num} x {c} = {num*c}')
