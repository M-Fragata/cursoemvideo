from math import sqrt
import random

##number = int(input('Digite um número: '))
number = random.randint(1, 10) * random.randint(1, 10)

print('A raiz quadrada de {} é de {:.1f}'.format(number, sqrt(number)))