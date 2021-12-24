import re

re_pair = r'\[([\s\S]*?)\]'
re_left = r'(\d+)(?!.*\d)'
re_right = r'(\d)'


class BinNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.num = data

    def PrintTree(self):
        print(self.num)


def addition(snail1, snail2):
    return '['+snail1 + ',' + snail2+']'


def explode(snail):
    depth = 0
    prev_brack = ''
    left_num = None
    right_num = None
    pair_match = None
    pair_pos = None
    exploded_snail = snail
    for i, s in enumerate(snail):
        if s == '[':
            depth += 1
            prev_brack = '['
            if depth == 4:
                pair_match = re.search(re_pair, snail[i+1:])
                left_match = re.search(re_left, snail[:i+pair_match.start()])
                right_match = re.search(re_right, snail[i+pair_match.end():])

                if pair_match is not None:
                    pair = pair_match.group()[1:-1].split(',')
                    exploded_pair = [0, 0]
                    print(left_match)
                    if left_match is not None:
                        exploded_pair[0] = int(
                            left_match.group()) + int(pair[0])
                    if right_match is not None:
                        exploded_pair[1] = int(
                            right_match.group()) + int(pair[1])
                    print(pair)
                    print(exploded_pair)

                break

        elif s == ']':
            if prev_brack == '[':
                depth -= 1
                prev_brack = ']'

    return depth


def part_one():
    str1 = '[1,2]'
    str2 = '[[3,4],5]'
    str3 = '[[[[[9,8],1],2],3],4]'
    str4 = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'

    print(explode(str4))

    with open("test", "r") as f:

        line = f.readline().strip()


part_one()
