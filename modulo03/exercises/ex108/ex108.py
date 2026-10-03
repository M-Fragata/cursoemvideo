## Adaptew o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

import moeda

num = float(input('Digite o preço: R$'))

print(f"Aumentando 10%, temos {moeda.real(moeda.aumentar(num))}")
print(f"Diminuindo 13%, temos {moeda.real(moeda.diminuir(num))}")
print(f"O dobro de {num} é {moeda.real(moeda.dobro(num))}")
print(f"A metade de {num} é {moeda.real(moeda.metade(num))}")