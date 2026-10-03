def leiadinheiro(msg):
    while True:
        num = input(msg).replace(',','.')
        if num.replace('.','').isnumeric():
            return float(num)

        print(f'ERRO: "{num}" é um preço inválido!')
