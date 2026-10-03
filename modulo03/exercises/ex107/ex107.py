## Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade().
## Faça também um programa que importa esse módulo e use algumas dessas funções.

import moeda

num = float(input('Digite o preço: R$'))

print(f"Aumentando 10%, temos {moeda.aumentar(num)}")
print(f"Diminuindo 13%, temos {moeda.diminuir(num)}")
print(f"O dobro de {num} é {moeda.dobro(num)}")
print(f"A metade de {num} é {moeda.metade(num):.2f}")
