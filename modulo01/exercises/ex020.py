##O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

def main():
    randomstudent: str = choice(alunos)
    alunos.remove(randomstudent)
    return randomstudent

counter: int = 0

while counter < 4:
    student = main()
    print('{}º aluno: {}'.format(counter + 1, student))
    counter += 1