## Crie um programa que faça o computador jogar JOKENPÔ com você.
import random

def pedra(machine):
    status = f"You Win!" if machine == 'Tesoura' else 'You Lose!' if machine == 'Papel' else 'Draw!'
    return status

def papel(machine):
    status = f"You Win!" if machine == 'Pedra' else 'You Lose!' if machine == 'Tesoura' else 'Draw!'
    return status

def tesoura(machine):
    status = f"You Win!" if machine == 'Papel' else 'You Lose!' if machine == 'Pedra' else 'Draw!'
    return status

def main():

    jogador = str(input('Pedra, Papel ou Tesoura? ')).title().strip()

    machine = random.randint(1,3)
    jogada_machine = 'Pedra' if machine == 1 else 'Papel' if machine == 2 else 'Tesoura'

    print(f"You: {jogador}\nMachine: {jogada_machine}")

    if jogador == 'Pedra':
        print(pedra(jogada_machine))
    elif jogador == 'Papel':
        print(papel(jogada_machine))
    elif jogador == 'Tesoura':
        print(tesoura(jogada_machine))
    else:
        print('Jogada inválida!')

main()