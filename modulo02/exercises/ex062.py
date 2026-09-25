## Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

status = True

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

contador1 = 1
contador2 = 10

while status: 

    while contador1 <= contador2:
        print(f"{contador1}º termo: {termo}")
        contador1 += 1
        termo = termo + razao

    continuar = int(input(f"Informe '0' se deseja parar ou informe a quantidade de termos a mais que deseja ver: "))
    if continuar == 0:
        print(f"Desligando programa...")
        break

    contador2 = contador2 + continuar
