## Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

counter = 1
s1 = 1
s2 = 0

user_num = int(input('Até qual número deseja saber a sequencia Fibonacci? '))

while counter <= user_num:
    if counter == 1:
        print(0, end=' -> ')
    elif counter == 2:
        print(1, end=' -> ')
    else:
        s1, s2 = s1 + s2, s1
        print(s1, end=' -> ')

    counter += 1
    
print('FIM')