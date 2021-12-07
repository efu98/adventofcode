import numpy as np


def sum_fuel(x):
    return (x*(x+1))/2


def part_one():
    with open("test", "r") as f:
        values = f.readline()
        values = np.array([int(val) for val in values.split(',')])

        least_fuel = np.ones(values.shape[0])*int(np.median(values))
        diff_array = np.absolute(
            np.diff(np.stack((values, least_fuel)), axis=0)[0])

    return int(diff_array.sum())


def part_two():
    with open("input", "r") as f:
        values = f.readline()
        values = np.array([int(val) for val in values.split(',')])

        uniq, count = np.unique(values, return_counts=True)

        min_fuel = np.inf

        for val in range(values.max()+1):

            least_fuel = np.ones(values.shape[0])*round(val)
            diff_array = np.absolute(
                np.diff(np.stack((values, least_fuel)), axis=0)[0])
            diff_array = np.array([sum_fuel(d) for d in diff_array])
            total_fuel = int(diff_array.sum())
            if min_fuel > total_fuel:
                min_fuel = total_fuel

    return min_fuel


print(part_one())
