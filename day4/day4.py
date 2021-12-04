import numpy as np
import re

BINGO_SIZE = 5


def part_one():
    with open("input", "r") as f:
        values = f.readlines()

        drawn_number = np.array(values[0].split(','), dtype=int)

        # shape values as a array of matrix of size 5, 5
        values = np.array(values[1:])
        values = values[values[:] != '\n']
        values = np.array(
            list(map(lambda x: re.split('(?<=\\S) ', x.strip()), values)), dtype=int)
        values = values.reshape(
            int(values.shape[0]/BINGO_SIZE), BINGO_SIZE, BINGO_SIZE)

        # create a matrix of booleans where true are checked numbers and
        # false are unchecked ones
        checked_values = np.zeros(values.shape, dtype=bool)

        # drawing numbers
        for nb in drawn_number:
            checked_values = np.logical_or(checked_values, (values[:] == nb))

            # check which columns and rows are fully checked
            full_column = np.all(checked_values, axis=1)
            full_row = np.all(checked_values, axis=2)

            # if one column is full
            if np.any(full_column):
                # get the winning board
                values = values[np.nonzero(full_column)[0]][0]
                checked_values = checked_values[np.nonzero(full_column)[0]][0]

                return(values[~checked_values].sum()*nb)

            # if one row is full
            if np.any(full_row):
                # get the winning board
                values = values[np.nonzero(full_row)[0]][0]
                checked_values = checked_values[np.nonzero(full_row)[0]][0]

                return(values[~checked_values].sum()*nb)


def part_two():
    with open("input", "r") as f:
        values = f.readlines()

        drawn_number = np.array(values[0].split(','), dtype=int)

        # shape values as a array of matrix of size 5, 5
        values = np.array(values[1:])
        values = values[values[:] != '\n']
        values = np.array(list(map(lambda x: re.split('(?<=\\S) ', x.strip()), values)), dtype=int)
        values = values.reshape(
            int(values.shape[0]/BINGO_SIZE), BINGO_SIZE, BINGO_SIZE)

        # create a matrix of booleans where true are checked numbers and
        # false are unchecked ones
        checked_values = np.zeros(values.shape, dtype=bool)

        for nb in drawn_number:
            checked_values = np.logical_or(checked_values, (values[:] == nb))

            full_column = np.all(checked_values, axis=1)
            full_row = np.all(checked_values, axis=2)
            if values.shape[0] > 1:
                if np.any(full_column):
                    values = np.delete(
                        values, np.nonzero(full_column)[0], axis=0)
                    checked_values = np.delete(
                        checked_values, np.nonzero(full_column)[0], axis=0)

                elif np.any(full_row):
                    values = np.delete(values, np.nonzero(full_row)[0], axis=0)
                    checked_values = np.delete(
                        checked_values, np.nonzero(full_row)[0], axis=0)
            elif values.shape[0] == 1:
                if np.any(full_column) or np.any(full_row):
                    return(values[~checked_values].sum()*nb)


print(part_two())
