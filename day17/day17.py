def probe_throw(pos, velocity):
    pos[0] += velocity[0]
    pos[1] += velocity[1]

    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1

    velocity[1] -= 1

    return pos, velocity


def part_one():

    with open("input", "r") as f:
        target = f.readline().strip()
        target = target.replace('target area: ', '').split(', ')
        target_x = [int(val)
                    for val in target[0].replace('x=', '').split('..')]
        target_y = [int(val)
                    for val in target[1].replace('y=', '').split('..')]

        max_pos = -9999

        for i in range(0, target_x[1]):
            for j in range(target_y[0], -target_y[1]):
                velocity = [i, j]
                pos = [0, 0]

                while pos[0] < target_x[1] and pos[1] > target_y[0]:

                    pos, velocity = probe_throw(pos, velocity)
                    if pos[0] >= target_x[0] and pos[0] <= target_x[1] and pos[1] >= target_y[0] and pos[1] <= target_y[1]:
                        print(pos)
                        if j*(j+1)/2 > max_pos:
                            max_pos = j*(j+1)/2

        print(max_pos)


def part_two():

    with open("input", "r") as f:
        target = f.readline().strip()
        target = target.replace('target area: ', '').split(', ')
        target_x = [int(val)
                    for val in target[0].replace('x=', '').split('..')]
        target_y = [int(val)
                    for val in target[1].replace('y=', '').split('..')]

        possible = set()

        for i in range(0, target_x[1]+1):
            for j in range(target_y[0], -target_y[0]+1):
                velocity = [i, j]
                pos = [0, 0]

                while pos[0] < target_x[1] and pos[1] > target_y[0]:

                    pos, velocity = probe_throw(pos, velocity)
                    if pos[0] >= target_x[0] and pos[0] <= target_x[1] and pos[1] >= target_y[0] and pos[1] <= target_y[1]:
                        possible.add((i, j))
        print(possible)
        print(len(possible))


part_two()
