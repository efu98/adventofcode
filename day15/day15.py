import numpy as np


def find_neighbors(s, width, height):
    if s[1] < width - 1:
        yield (s[0], s[1]+1)
    if s[1] > 0:
        yield (s[0], s[1]-1)
    if s[0] < height - 1:
        yield (s[0]+1, s[1])
    if s[0] > 0:
        yield (s[0]-1, s[1])


def find_path_risk(width, height, risk_level, previous):
    A = []
    s = (height-1, width-1)

    while s != (0, 0):
        A.append(risk_level[s[0]][s[1]])
        s = previous[s]

    return A


def dijkstra(width, height, risk_level):
    d = {}
    for i in range(width):
        for j in range(height):
            d[(i, j)] = 99999
    d[(0, 0)] = 0

    not_visited = [(0, (0, 0))]
    previous = {}
    while len(not_visited) > 0:

        current = not_visited[0][1]
        not_visited.pop(0)

        for neighbor in find_neighbors(current, width, height):
            distance = d[current] + risk_level[neighbor[0]][neighbor[1]]
            if d[neighbor] > distance:
                d[neighbor] = distance
                not_visited.append((distance, neighbor))
                previous[neighbor] = current

        not_visited.sort()

    return(previous)


def level_wrap(level, offset):
    level = level+offset
    if level >= 10:
        level = level % 9
    return level


def part_one():
    with open("input", "r") as f:
        risk_level = f.readlines()

        risk_level = [[int(val) for val in list(risk.strip())]
                      for risk in risk_level]

    width = len(risk_level[0])
    height = len(risk_level)

    previous = dijkstra(width, height, risk_level)

    return sum(find_path_risk(width, height, risk_level, previous))


def part_two():
    with open("test", "r") as f:
        risk_level = f.readlines()

        risk_level = [[int(val) for val in list(risk.strip())]
                      for risk in risk_level]

    tiles = [[i+j for i in range(0, 5)] for j in range(0, 5)]

    extend_risk = []
    extend_row = risk_level
    for row in tiles:
        for tile in row:
            extend_row = np.concatenate((extend_row, [[level_wrap(val, tile)
                                                       for val in risk] for risk in risk_level]), axis=1)

        print(extend_row)
        extend_row = []


print(part_two())
