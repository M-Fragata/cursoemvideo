## Aprendendo laços em python

for c in range(0,6):
    print('Hello world')
print('Fim 1')

for c in range(6,0, -1):
    print('Hello world')
print('Fim 2')

for c in range(0, 6, 2):
    print('Hello world')
print('Fim 3')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim 4')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim 5')

s = 0
l = []
for c in range(1, 6):
    n = int(input('Digite um valor: '))
    s += n
    l.append(n)
print('O somatório de todos os valores foi {}'.format(s))
print('Os valores digitados foram: {}'.format(l))
print('Fim 6')