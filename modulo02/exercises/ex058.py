## Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print(f"Irei pensar em um número de 0 a 10 e você deve adivinhar no menor número de tentativas!")

aleatorio = randint(0,10)
user = 11
tentativas = 0

while user != aleatorio:
    user = int(input(f"Digite um número de 0 a 10: "))
    tentativas += 1
    if user == aleatorio:
        print('=-='*13)
        print(f"Parabéns! você acertou na {tentativas}º tentativa")
        print('=-='*13)
        break
    print(f"Errou! Tente novamente!")
