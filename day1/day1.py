def part_one():
    with open("input", "r") as f:
        line = f.readline()
        prev = int(line)
        inc = 0

        line = f.readline()

        while line:
            x = int(line)
            if prev < x:
                inc += 1
            prev = x
            line = f.readline()

    return inc


def part_two():
    prev = 0
    inc = 0
    with open("input", "r") as f:
        pointer = f.tell()
        for _ in range(3):
            prev += int(f.readline())
        print(prev)
        f.seek(pointer)

        line = f.readline()

        while line:
            three_measurements = int(line)
            pointer = f.tell()

            for _ in range(2):
                line = f.readline()
                if line != '':
                    three_measurements += int(line)

            if prev < three_measurements:
                inc += 1
            prev = three_measurements
            f.seek(pointer)

            line = f.readline()

        return(inc)
