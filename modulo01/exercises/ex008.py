##Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros;

metric = float(input('Enter a metric in meters: '))


def main(meters):
    print('KM: {}'.format(metric / 1000))
    print('HM: {}'.format(metric / 100))
    print('DAM: {}'.format(metric / 10))
    print('M: {}'.format(metric / 1))
    print('DM: {}'.format(metric * 10))
    print('CM: {}'.format(metric * 100))
    print('MM: {}'.format(metric * 1000))


main(metric)
