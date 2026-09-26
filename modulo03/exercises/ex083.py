##  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = input('Informe a fórmula: ')

pilha = []
status = True

for caractere in expression:
    if caractere == '(':
        pilha.append('(')
    elif caractere ==')':
        if '(' in pilha:
            pilha.pop()
        else:
            status = False
            break

if status:
    print('Expressão Válida!')
else: 
    print('Expressão Inválida!')