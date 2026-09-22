## Faça um programa que leia uma frase pelo teclado e mostre:
## Quantas vezes aparece a letra "A"
## Em que posição aparece a primeira vez
## Em que posição ela aparece a última vez

def main():

    phrase = input("Enter a phrase: ").strip()
    a_times = phrase.upper().count("A")
    a_firsttime = phrase.upper().find("A") + 1
    a_lasttime = phrase.upper().rfind("A") + 1

    print(a_times, a_firsttime, a_lasttime)
main()