def sort_coord(coord1, coord2):
    if coord1 > coord2:
        return(coord2, coord1)
    return(coord1, coord2)


def part_one():
    with open("input", "r") as f:
        values = f.readlines()

        # shape values into array of array of two coordinates (start and end)
        values = [[[int(coord) for coord in points.split(',')] for points in line.split(' -> ')]
                  for line in values]

        # create diagram
        diagram = [[0 for _ in range(999)] for _ in range(999)]

        # filling the diagram
        for line in values:
            # same x -> vertical line
            if line[0][0] == line[1][0]:
                sorted_coord = sort_coord(line[0][1], line[1][1])
                for point in range(sorted_coord[0], sorted_coord[1]+1):
                    diagram[line[0][0]][point] += 1

            # same y -> horizontal line
            elif line[0][1] == line[1][1]:
                sorted_coord = sort_coord(line[0][0], line[1][0])
                for point in range(sorted_coord[0], sorted_coord[1]+1):
                    diagram[point][line[0][1]] += 1

        # counting points where lines overlap
        count = sum([len([1 for point in line if point > 1])
                    for line in diagram])

    return(count)


def part_two():
    with open("input", "r") as f:
        values = f.readlines()

        # shape values into array of array of two coordinates (start and end)
        values = [[[int(coord) for coord in points.split(',')] for points in line.split(' -> ')]
                  for line in values]

        # create diagram
        diagram = [[0 for _ in range(999)] for _ in range(999)]

        # filling the diagram
        for line in values:
            steps = abs(line[0][1] - line[1][1])
            # direction of x
            if line[0][0] == line[1][0]:
                dir_x = 0
            elif line[0][0] < line[1][0]:
                dir_x = 1
            else:
                dir_x = -1

            # direction of y
            if line[0][1] == line[1][1]:
                dir_y = 0
                steps = abs(line[0][0] - line[1][0])
            elif line[0][1] < line[1][1]:
                dir_y = 1
            else:
                dir_y = -1

            # fill diagram
            for step in range(steps+1):
                diagram[line[0][0]+step*dir_x][line[0][1]+step*dir_y] += 1

        # counting points where lines overlap
        count = sum([len([1 for point in line if point > 1])
                    for line in diagram])

    return(count)


print(part_two())
