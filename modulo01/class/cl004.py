## Manipulação de textos

frase = 'Curso em Vídeo Python'

print(frase[:5])
print(frase[5:])
print(frase[5::2])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
frase.replace('python','android')
frase.upper()
frase.lower()
frase.capitalize() ##primeira letra de cada palavra maiuscula
frase.title()

frase2 = '   aprenda python  '
frase2.strip()
frase2.rstrip() ##tratamento do lado direito apenas
frase2.lstrip() ##tratamento do lado esquerdo apenas
frase.split()
'-'.join(frase)
frase.find('python')