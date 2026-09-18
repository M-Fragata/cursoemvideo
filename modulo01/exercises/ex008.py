##Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros;

metric = float(input('Enter a metric in meters: '))


def main(meters):
    print('The metric {} in cm is {}'.format(meters, convert('cm', meters)))
    print('The metric {} in mm is {}'.format(meters, convert('mm', meters)))

def convert(unit, meters):
    if unit == 'cm':
        return meters * 100
    elif unit == 'mm':
        return meters * 1000

main(metric)