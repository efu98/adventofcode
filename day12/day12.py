possible_paths = []
cave_node = {}

# create a dictionnary with each nodes and its neighbors
with open("input", "r") as f:
    cave_map = f.readlines()
    cave_map = [row.strip().split('-') for row in cave_map]

    for row in cave_map:
        if row[1] not in cave_node:
            cave_node[row[1]] = []
        if row[0] not in cave_node:
            cave_node[row[0]] = []
        cave_node[row[0]].append(row[1])
        cave_node[row[1]].append(row[0])


# recursive function for the first part of the challenge
# explore possible paths for each nodes
def explore(current_node, path):
    path += current_node
    # stopping condition : the current node is the end of the graph
    if current_node == 'end':
        possible_paths.append(path)

    else:
        # explore each neighbors of the current node
        for neighbor in cave_node[current_node]:
            # if neighbor is not in path or neighbor is a big cave
            if neighbor not in path or neighbor.upper() == neighbor:
                explore(neighbor, path)


# recursive function for the second part of the challenge
# explore possible paths for each nodes
# visited_twice is a boolean that checks if a small cave has been visited twice
def explore_twice(current_node, path, visited_twice):

    path += current_node
    # stopping condition : the current node is the end of the graph
    if current_node == 'end':
        possible_paths.append(path)

    else:
        # explore each neighbors of the current node
        for neighbor in cave_node[current_node]:
            # if neighbor is not in path or neighbor is a big cave
            if neighbor not in path or neighbor.upper() == neighbor:
                explore_twice(neighbor, path, visited_twice)

            # if no cave has been visited twice and the neighbor is not the
            # start or the end node
            elif visited_twice is False and neighbor != 'start' and neighbor != 'end':
                explore_twice(neighbor, path, True)


def part_one():
    explore('start', '')
    return len(possible_paths)


def part_two():
    explore_twice('start', '', False)
    return len(possible_paths)


print(part_two())
