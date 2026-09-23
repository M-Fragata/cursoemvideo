## Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
##menor que 18.5: Abaixo do peso
##Entre 18.5 e 25: Peso ideal
## 25 até 30: sobrepeso
## 30 até 40: obesidade
##Acima de 40: Obesidade morbida

def main():

    altura = float(input('Qual a sua altura? '))
    peso = float(input('Qual o seu peso? '))

    imc = peso / (altura * altura)

    print(f"IMC de: {imc:.2f}")
    print(f"Abaixo do peso" if imc <= 18.5 else f"Peso ideal" if imc > 18.5 and imc <= 25 else f"Sobrepeso" if imc > 25 and imc <= 30 else f"Obesidade" if imc > 30 and imc <= 40 else f"Obesidade morbida")

main()