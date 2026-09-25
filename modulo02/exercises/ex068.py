## Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

counter = 1

while True:
    rand = randint(0,10)

    print('Vamos jogar Par ou Impar!')
    num = int(input('Informe seu número de 0 a 10: '))
    choice = input('Escolha Par ou Impar: ').title().strip()

    status = True if (num+rand)%2==0 else False
    result = True if status and choice == 'Par' else False

    print('=-='*10)
    print('Tabela das Jogadas: ')
    print(f'Você: {num} - {choice}')
    print(f'Máquina: {rand} - Par' if choice == 'Impar' else f'Máquina: {rand} - Impar')
    print(f'Resultado: ')
    print(f'{num+rand} é Par' if status else f'{num+rand} é Impar')
    if not result:
        print('Você perdeu!')
        print('=-='*10)
        break
    print('Você Ganhou! Continue!')
    print('=-='*10)
    counter += 1
print(f'Total de partidas jogadas: {counter}')
    