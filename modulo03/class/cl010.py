## Listas (array)

num = [2, 5, 9, 1]
print(num)
num[2] = 15
num.append(10) ## adiciona por ultimo
num.insert(0,99) ## adiciona no inicio com o zero
print(num)
num.sort()
print(num)
len(num) 
num.pop() ## elimina o ultimo elemento
num.pop(2) ## elimina um elemento especifico informando o index
num.remove(2) ## neste caso irá eliminar o primeiro nº 2 que encontrar

if 4 in num:
    num.remove(4)
else:
    print('Não há número 4 na lista')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for valor in valores:
    print(f'{valor}', end=' -> ')
print('FIM')

for index, valor in enumerate(valores):
    print(f'Na posição {index} encontrei o valor {valor}!')
print('Cheguei ao final da lista!')

## Ao fazer uma igualdade entre listas ocorre uma ligação entre elas e quando uma é alterada a outra também é
a = [2, 3, 4, 7]
b = a ## utilizando a forma b = a[:] irá criar uma cópia de a dentro de b, nao havendo ligação entre eles
b[2] = 8
print(f'Lista a: {a}')
print(f'Lista b: {b}')