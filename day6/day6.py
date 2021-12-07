def part_one():
    with open("input", "r") as f:
        values = f.readline()
        values = [int(val) for val in values.split(',')]

        for i in range(80):
            for fish in range(len(values)):
                if values[fish] == 0:
                    values[fish] = 6
                    values.append(8)
                else:
                    values[fish] -= 1

    return(len(values))


def part_two():
    with open("input", "r") as f:
        values = f.readline()
        values = [int(val) for val in values.split(',')]

        fishes = [0 for _ in range(9)]

        for fish in values:
            fishes[fish] += 1

        for _ in range(256):
            fishes_age0 = fishes[0]
            fishes.append(fishes.pop(0))
            fishes[6] += fishes_age0
            print(fishes)

    return(sum(fishes))


print(part_two())
