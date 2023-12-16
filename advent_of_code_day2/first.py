RED = 12
GREEN = 13
BLUE = 14


def main():
    with open('input.txt') as f:
        input = f.read().splitlines()
    sum = 0
    for line in input:
        id = line.split(':')[0]
        line = line.split(':')[1]
        list = [line.split(',')]
        sets = line.split(';')

        


main()