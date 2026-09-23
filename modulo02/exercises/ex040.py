## Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média. - abaixo de 5 reprovado; - entre 5 e 6.9 recuperação e 7 ou mais aprovado

def main():

    nota1 = float(input('whats your first nota? '))
    nota2 = float(input('whats your second nota? '))

    media = (nota1 + nota2) / 2
    aprovar = 7
    reprovar = 5

    print(f"Média de: {media} pontos")
    print(f"Aprovado!" if media >= aprovar else "Reprovado!" if media < reprovar else "Recuperação!")

main()