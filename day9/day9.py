import math


def part_one():
    with open("input", "r") as f:
        heightmap = f.readlines()
        heightmap = [list(row.strip())for row in heightmap]
        heightmap = [[9]+[int(point) for point in row]+[9]
                     for row in heightmap]

        heightmap = [[9 for _ in range(
            len(heightmap[0]))]] + heightmap + [[9 for _ in range(len(heightmap[0]))]]

        min_points = []

        neighbor_size = 1

        for i in range(1, len(heightmap)-1):
            for j in range(1, len(heightmap[0])-1):
                neighbors = []
                for window_i in range(-neighbor_size+i, neighbor_size+i+1):
                    for window_j in range(-neighbor_size+j, neighbor_size+j+1):
                        neighbors.append(heightmap[window_i][window_j])
                if heightmap[i][j] == min(neighbors) and all(n == neighbors[0] for n in neighbors) == False:
                    print(neighbors)
                    print(heightmap[i][j])
                    print((i, j))
                    min_points.append(heightmap[i][j]+1)
        return(sum(min_points))


def find_basin(i, j, heightmap, basin):
    if heightmap[i][j] == 9 or (i, j) in basin:
        return 0
    else:
        basin.add((i, j))
        return 1 + find_basin(i, j+1, heightmap, basin) + find_basin(i+1, j, heightmap, basin) + find_basin(i-1, j, heightmap, basin) + find_basin(i, j-1, heightmap, basin)


def part_two():
    with open("input", "r") as f:
        heightmap = f.readlines()
        heightmap = [list(row.strip())for row in heightmap]
        heightmap = [[9]+[int(point) for point in row]+[9]
                     for row in heightmap]

        heightmap = [[9 for _ in range(
            len(heightmap[0]))]] + heightmap + [[9 for _ in range(len(heightmap[0]))]]

        min_coords = []

        neighbor_size = 1
        basins = []

        for i in range(1, len(heightmap)-1):
            for j in range(1, len(heightmap[0])-1):
                neighbors = []
                for window_i in range(-neighbor_size+i, neighbor_size+i+1):
                    for window_j in range(-neighbor_size+j, neighbor_size+j+1):
                        neighbors.append(heightmap[window_i][window_j])
                if heightmap[i][j] == min(neighbors) and all(n == neighbors[0] for n in neighbors) == False:
                    min_coords.append((i, j))

        for point in min_coords:
            basins.append(find_basin(point[0], point[1]-1, heightmap, set()))

        basins = sorted(basins)
        print(basins[-3:])

        return math.prod(basins[-3:])


print(part_two())
