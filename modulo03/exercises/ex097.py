## Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(content):
    t = len(content) + 6
    print("-"* t)
    print(f"   {content}   ")
    print("-"* t)
escreva("Hello, world!")
escreva("Estou estudando python!")
escreva("Analista de dados")