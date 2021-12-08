def part_one():
    with open("input", "r") as f:
        values = f.readlines()
        values = [[val.split()for val in signal.split(' | ')]
                  for signal in values]

        # count the numbers of obvious numbers (1, 4, 7, 8) in the input
        count = 0
        for output in values:
            for signal in output[1]:
                if len(signal) in [2, 4, 3, 7]:
                    count += 1

        return(count)


def part_two():
    with open("input", "r") as f:
        values = f.readlines()
        values = [[val.split()for val in signal.split(' | ')]
                  for signal in values]

        number_dict = {}
        all_output = []
        for output in values:
            # add obvious numbers to the dictionary
            for signal in output[0]:
                if len(signal) == 2:
                    number_dict['1'] = "". join(sorted(signal))
                if len(signal) == 4:
                    number_dict['4'] = "". join(sorted(signal))
                if len(signal) == 3:
                    number_dict['7'] = "". join(sorted(signal))
                if len(signal) == 7:
                    number_dict['8'] = "". join(sorted(signal))

            # get remarkable elements to find other numbers
            # union4_7 is used to find 9
            # diff4_7 is used to find 5
            union4_7 = sorted(set(number_dict['4'] + number_dict['7']))
            diff4_7 = list(set(number_dict['4']).difference(
                set(number_dict['7'])))

            for signal in output[0]:
                # find numbers that have 5 segments
                if len(signal) == 5:
                    if all(wire in signal for wire in diff4_7):
                        number_dict['5'] = "". join(sorted(signal))
                    elif all(wire in signal for wire in list(number_dict['7'])):
                        number_dict['3'] = "". join(sorted(signal))
                    else:
                        number_dict['2'] = "". join(sorted(signal))

                # find numbers that have 6 segments
                if len(signal) == 6:

                    if all(wire in signal for wire in union4_7):
                        number_dict['9'] = "". join(sorted(signal))
                    elif all(wire in signal for wire in list(number_dict['7'])):
                        number_dict['0'] = "". join(sorted(signal))
                    else:
                        number_dict['6'] = "". join(sorted(signal))

            # get the output value
            output_val = ""
            for signal in output[1]:
                for value, wire in number_dict.items():
                    if wire == "".join(sorted(signal)):
                        output_val += value

            all_output.append(int(output_val))
            number_dict = {}

        return sum(all_output)


print(part_two())
