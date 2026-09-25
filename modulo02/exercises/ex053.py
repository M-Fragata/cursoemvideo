## Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

phrase = str(input('Informe uma frase curta: ')).strip().upper()
n = phrase.replace(" ", "")

status = True
tamanho_frase = len(n) -1

for c in range (0, len(n)):
    status = True if n[c] == n[tamanho_frase - c] else False
    if not status:
        break

print(f"A frase '{phrase}' trata-se de um palíndromo" if status else f"A frase '{phrase}' NÃO trata-se de um palíndromo")


## Outro jeito
n_invertido = n[::-1] ## Inverte a frase completamente
print(f"A frase '{phrase}' trata-se de um palíndromo" if n_invertido == n else f"A frase '{phrase}' NÃO trata-se de um palíndromo")