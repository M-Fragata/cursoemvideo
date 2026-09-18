something = input('Enter something: ')

def main():
    print('"{}", its the type: {}'.format(something, type(something)))
    print('"{}", do only have spaces? {}'.format(something, something.isspace()))
    print('"{}", its a number? {}'.format(something, something.isnumeric()))
    print('"{}", its alphabetic? {}'.format(something, something.isalpha()))
    print('"{}", its a alphanum? {}'.format(something, something.isalnum()))
    print('"{}", its supper? {}'.format(something, something.isupper()))
    print('"{}", its lower? {}'.format(something, something.islower()))
    print('"{}", its a title? {}'.format(something, something.istitle()))
main()