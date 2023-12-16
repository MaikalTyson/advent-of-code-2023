RED = 12
GREEN = 13
BLUE = 14


def main():
    with open('input.txt') as f:
        input = f.read().splitlines()
    games = set()
    for line in input:
        id, line_arr = line.split(':')[0], line.split(':')[1].split(';')
        for cubes in line_arr:
            index = int(id.split(' ')[1])
            games.add(index)

    valid = 0
    for line in input:
        id, line_arr = line.split(':')[0], line.split(':')[1].split(';')
        for cubes in line_arr:
            index = int(id.split(' ')[1])
            
            cubes = cubes.strip()
            cube = cubes.split(', ')

            for c in cube:
                if valid == 1:
                    break
                value = int(c.split(' ')[0])
                color = c.split(' ')[1]
                if color == 'red' and value > RED:
                    games.remove(index)
                    valid = 1
                    break
                elif color == 'green' and value > GREEN:
                    games.remove(index)
                    valid = 1
                    break
                elif color == 'blue' and value > BLUE:
                    games.remove(index)
                    valid = 1
                    break
        valid = 0
    res = [game for game in games]
    sum = 0
    for r in res:
        sum += r
    print(sum)


main()