## Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

status = True

while status:
    sexo = input(f"Informe seu sexo\n'M' para masculino\n'F' para feminino\n").upper().strip()
    if sexo in ['M', 'F']:
        status = False
        print(f"Usuário é do sexo '{sexo}'")
    else:
        print(f"Sexo invalido! Tente novamente!")