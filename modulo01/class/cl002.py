##Operators Arithmetics
n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \n o product é {} \n e a divisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))