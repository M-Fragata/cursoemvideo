## Colorindo o terminal
## \033[0;33;44 m style;text;bg
## style: 0 nada;1 bold;4 underline;7 negative
## text: 30 branco; 31 vermelho; 32 verde; 33 amarelo; 34 azul; 35 roxo; 36 azul claro; 37 cinza
## bg: 40-47 mesma ordem de cores do text

print('\033[7;31;43mOlá, mundo!\033[m')

nome = 'Matheus'
print(f"Olá! muito prazer em te conhecer, \33[1;32;40m{nome}\33[m!!")