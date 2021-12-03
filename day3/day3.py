import numpy as np


def part_one():
    with open("input", "r") as f:
        values = f.readlines()
        values = np.array(
            list(map(lambda x: np.array(list(x.strip()), dtype=int), values)))

        # count the number of zeros and one per columns
        one_count = np.count_nonzero(values == 1, axis=0)
        zero_count = np.count_nonzero(values == 0, axis=0)

        # get gamma rate as a binary number by comparing the number of zeros and
        # the number of ones
        gamma_rate = 1*np.greater(one_count, zero_count)
        epsilon_rate = 1*np.greater(zero_count, one_count)

        # convert binary number to int
        gamma_rate = gamma_rate.dot(2**np.arange(gamma_rate.size)[::-1])
        epsilon_rate = epsilon_rate.dot(2**np.arange(epsilon_rate.size)[::-1])

    return(gamma_rate*epsilon_rate)


def part_two():
    with open("input", "r") as f:
        o2 = f.readlines()
        o2 = np.array(
            list(map(lambda x: np.array(list(x.strip()), dtype=int), o2)))

        co2 = np.copy(o2)

        for i in range(o2.shape[1]):
            # count the number of zeros and one for column i in for o2 and co2
            one_count_o2 = np.count_nonzero(o2[:, i] == 1, axis=0)
            zero_count_o2 = np.count_nonzero(o2[:, i] == 0, axis=0)

            one_count_co2 = np.count_nonzero(co2[:, i] == 1, axis=0)
            zero_count_co2 = np.count_nonzero(co2[:, i] == 0, axis=0)

            # keep the rows starting with the right number
            if o2.shape[0] > 1:
                if one_count_o2 >= zero_count_o2:
                    o2 = o2[o2[:, i] == 1]
                else:
                    o2 = o2[o2[:, i] == 0]

            if co2.shape[0] > 1:
                if one_count_co2 >= zero_count_co2:
                    co2 = co2[co2[:, i] == 0]
                else:
                    co2 = co2[co2[:, i] == 1]

        # get the first value
        co2 = co2.flatten()
        o2 = o2.flatten()

        # convert binary number to int
        co2 = co2.dot(2**np.arange(co2.size)[::-1])
        o2 = o2.dot(2**np.arange(o2.size)[::-1])
    return(co2*o2)


print(part_two())
