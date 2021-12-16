with open("input", "r") as f:
    template = f.readline().strip()
    f.readline()
    transformations = {}

    for transformation in f.readlines():
        transformation = transformation.strip().split(' -> ')
        transformations[transformation[0]] = transformation[1]


def count_occurence(polymer):
    unique_elem = ''.join(set(polymer))

    occurence = {}

    for elem in unique_elem:
        occurence[elem] = polymer.count(elem)

    return occurence


def add_count(temp_count, prev_count):
    for key in temp_count:
        if key not in prev_count:
            prev_count[key] = temp_count[key]
        else:
            prev_count[key] += temp_count[key]

    return(prev_count)


def polymerization(temp, steps):
    for _ in range(steps):
        polymer = temp[0]
        for i in range(len(temp)-1):
            polymer += transformations[temp[i:i+2]] + temp[i+1]
        temp = polymer

    return temp


def part_one():

    polym_template = polymerization(template, 10)
    occurence = list(count_occurence(polym_template).values())
    print(occurence)

    return max(occurence) - min(occurence)


def part_two():
    pair_counter = {}

    for pair in transformations:
        pair_counter[pair] = template.count(pair)

    unique_elem = ''.join(set(''.join(list(transformations.keys()))))
    occurence = {}
    for elem in unique_elem:
        occurence[elem] = template.count(elem)

    for _ in range(40):
        for pair, count in pair_counter.copy().items():
            pair_counter[pair] -= count
            pair_counter[pair[0]+transformations[pair]] += count
            pair_counter[transformations[pair]+pair[1]] += count
            occurence[transformations[pair]] += count

    occurence = list(occurence.values())

    return max(occurence) - min(occurence)


print(part_two())
