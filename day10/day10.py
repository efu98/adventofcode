opening_char = ['(', '{', '<', '[']
closing_char = [')', '}', '>', ']']
closed_chunks = ['()', '{}', '<>', '[]']

# recursive function to remove closed chunks in line


def remove_closed_chunks(line):
    if any(chunk in line for chunk in closed_chunks):
        for chunk in closed_chunks:
            line = line.replace(chunk, '')
        return(remove_closed_chunks(line))
    return(line)


def part_one():

    score_table = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    with open("input", "r") as f:
        input = f.readlines()
        input = [line.strip() for line in input]

        points = []
        for line in input:
            # remove all the chunks that can be closed
            line = remove_closed_chunks(line)
            prev_char = ''
            for char in line:
                # checks if a closing char is in the line otherwise, they are
                # incomplete 
                # if yes, appends the score to the score table
                if char in closing_char:
                    points.append(score_table[char])
                    break
                prev_char = char

        return sum(points)


def part_two():
    score_table = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    with open("input", "r") as f:
        input = f.readlines()
        input = [line.strip() for line in input]

        scores = []
        for line in input:
            # remove all the chunks that can be closed
            line = remove_closed_chunks(line)
            # checks if all characters are opening char otherwise, they are
            # corrupted
            # if yes, compute the score
            if all(line_char in opening_char for line_char in line):
                score = 0
                for line_char in line[::-1]:
                    score = score * 5 + score_table[line_char]
                scores.append(score)

        # sort the scores to return the value in the middle of the array
        scores = sorted(scores)
        return scores[int(len(scores)/2)]


print(part_two())
