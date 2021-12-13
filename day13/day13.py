with open("input", "r") as f:

    input = f.readlines()
    input.remove('\n')

    instructions = []
    paper = []

    for row in input:
        if "fold along" not in row:
            paper.append([int(coord) for coord in row.split(',')])
        else:
            instructions.append(row.replace('fold along ', '').split('='))

    instructions = [[instr[0], int(instr[1])] for instr in instructions]


# fold the paper according to the instructions
def fold_instruction(instr):
    if instr[0] == 'y':
        for i in range(len(paper)):
            if paper[i][1] > instr[1]:
                paper[i][1] = 2*instr[1]-paper[i][1]

    if instr[0] == 'x':
        for i in range(len(paper)):
            if paper[i][0] > instr[1]:
                paper[i][0] = 2*instr[1]-paper[i][0]


def part_one():

    # fold the paper once
    fold_instruction(instructions[0])

    # count the nuber of dots
    unique_dots = []
    for dot in paper:
        if dot not in unique_dots:
            unique_dots.append(dot)

    return(len(unique_dots))


def part_two():

    # fold the paper following all the instructions
    for instr in instructions:
        fold_instruction(instr)

    # get the last fold of axis x and y to get the size of the screen
    shape_x = 0
    shape_y = 0
    for instr in reversed(instructions):
        if instr[0] == 'y':
            shape_y = instr[1]
            break
    for instr in reversed(instructions):
        if instr[0] == 'x':
            shape_x = instr[1]
            break

    # prepare display of the folded paper
    folded_paper = [['.' for _ in range(shape_x)] for _ in range(shape_y)]
    for dot in paper:
        folded_paper[dot[1]][dot[0]] = '#'

    return folded_paper


print(part_two())
