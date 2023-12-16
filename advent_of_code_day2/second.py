def main():
    with open('input.txt') as f:
        input = f.read().splitlines()

    red = [0,]
    green = [0,]
    blue = [0,]
    res, r, g, b = 0, 0, 0, 0
    for line in input:
        id, line_arr = line.split(':')[0], line.split(':')[1].split(';')
        for cubes in line_arr:
            index = int(id.split(' ')[1])
            
            cubes = cubes.strip()
            cube = cubes.split(', ')
            for c in cube:
                if c.split(' ')[1] == 'red':
                    red.append(int(c.split(' ')[0]))
                elif c.split(' ')[1] == 'green':
                    green.append(int(c.split(' ')[0]))
                elif c.split(' ')[1] == 'blue':
                    blue.append(int(c.split(' ')[0]))

        r += max(red)
        g += max(green)
        b += max(blue)
        res += r * g * b
        r, g, b, red, green, blue = 0, 0, 0, [], [], []
    print(res)


main()