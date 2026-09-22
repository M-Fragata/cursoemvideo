## condicionais aninhadas. ifs elifs e elses

nome = str(input('Qual é o seu nome? ')).title()

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Lucas' or nome == 'Matheus':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))