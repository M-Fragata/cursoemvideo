## Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para que o usuário tente descobrir qual foi o número escolhido pelo computador.
## O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

def main():
    machine = random.randint(1,5)
    user = int(input('Enter a number between 1 and 5: '))

    if user < 1 or user > 5:
        print('Invalid Number')
        return

    print(f"You: {user}, machine: {machine}")
    print('You Win!' if user == machine else 'You Lose!')

main()