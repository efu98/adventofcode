def part_one():
    with open("input", "r") as f:
        hor = 0
        depth = 0
        line = f.readline()
        while line:
            line = line.split()
            if line[0] == 'forward':
                hor += int(line[1])
            elif line[0] == 'down':
                depth += int(line[1])
            elif line[0] == 'up':
                depth -= int(line[1])

            line = f.readline()
    return hor*depth


def part_two():
    with open("input", "r") as f:
        hor = 0
        depth = 0
        aim = 0
        line = f.readline()
        while line:
            line = line.split()
            if line[0] == 'forward':
                hor += int(line[1])
                depth += aim*int(line[1])
            elif line[0] == 'down':
                aim += int(line[1])
            elif line[0] == 'up':
                aim -= int(line[1])

            line = f.readline()
    return hor*depth


print(part_two())
