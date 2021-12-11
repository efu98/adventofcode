import numpy as np

# Read input file
with open("input", "r") as f:
    energy = f.readlines()
    energy = [list(row.strip())for row in energy]

    # adding padding to the energy input
    energy = [[-1]+[int(point) for point in row]
              + [-1] for row in energy]
    energy = [[-1 for _ in range(len(energy[0]))]] + energy + \
        [[-1 for _ in range(len(energy[0]))]]

    energy = np.array(energy)


# Add energy octopus
# if octopus energy > 9, it adds energy to its neighbors and has an energy of -1
# so that it remains untouched

def illum(i, j):
    if energy[i][j] != -1:
        energy[i][j] += 1
        if energy[i][j] > 9:
            energy[i][j] = -1
            illum(i+1, j)
            illum(i-1, j)
            illum(i, j+1)
            illum(i, j-1)
            illum(i+1, j+1)
            illum(i-1, j-1)
            illum(i+1, j-1)
            illum(i-1, j+1)


def part_one():
    global energy

    count = 0
    for _ in range(100):
        for i in range(1, len(energy)-1):
            for j in range(1, len(energy[0])-1):
                illum(i, j)

        # converts octopus with energy -1 to 0
        for i in range(1, len(energy)-1):
            for j in range(1, len(energy[0])-1):
                if energy[i][j] == -1:
                    count += 1
                    energy[i][j] = 0

    return(count)


def part_two():
    global energy

    steps = 0
    while True:
        steps += 1
        for i in range(1, len(energy)-1):
            for j in range(1, len(energy[0])-1):
                illum(i, j)

        # if all energy all equal to -1, octopuses are in sync
        if (energy == -1).all():
            return(steps)

        # converts octopus with energy -1 to 0
        for i in range(1, len(energy)-1):
            for j in range(1, len(energy[0])-1):
                if energy[i][j] == -1:
                    energy[i][j] = 0


print(part_two())
