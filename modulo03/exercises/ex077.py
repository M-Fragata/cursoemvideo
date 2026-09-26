## Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.

palavras = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "curso",
    "estudar",
    "praticar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
    "sucesso"
)

for c in range(0, len(palavras)):
    word = palavras[c]
    print(f'{word:.<15}', end='')
    for letra in word:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print()