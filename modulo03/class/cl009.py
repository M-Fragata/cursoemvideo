## Aula de tuplas

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[-4])
print(lanche[0:2]) ## vai pegar o primeiro [0] e o segundo [1] ignora o 2
print(lanche[:4])
print(lanche[2:])

## As tuplas são imutáveis, então não é impossível alterá-las
for comida in lanche:
    print(comida)

for counter, comida in enumerate(lanche): ## enumerate precisa de 2 variáveis pois informa também o index
    print(comida)
    print(lanche[counter])

for counter in range(0, len(lanche)): ## enumerate precisa de 2 variáveis pois informa também o index
    print(counter)
    print(lanche[counter])

## mostrando a tupla em ordem alfabética utilizando sorted()
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(c.count(5))
print(c.index(8))

pessoa = ('Matheus', 25, 'M', 80)
##del(pessoa) ## é possível deletar tuplas
print(pessoa)