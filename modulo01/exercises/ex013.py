##Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salary = float(input('Whats your salary? '))

print('Seu salário atual de R${} com o aumento de 15% passará a ser R${}'.format(salary, salary + (salary * 0.15)))