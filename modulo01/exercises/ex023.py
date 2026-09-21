## Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
## Ex: 1834, unidade: 4 dezena: 3 centena 8 milhar 1

someNumber = int(input('Enter a number between 0 and 9999: '))

numberstr = str(someNumber).zfill(4)
size = len(numberstr)

def main():

    if someNumber < 0 or someNumber > 9999:
        print('Número inválido')
        return
    print(numberstr[0])
    milhar = numberstr[0]
    centena = numberstr[1]
    dezena = numberstr[2]
    unidade = numberstr[3]

    print(f'Milhar: {milhar}, Centena: {centena}: Dezena: {dezena}, Unidade: {unidade}')
    return
main()


