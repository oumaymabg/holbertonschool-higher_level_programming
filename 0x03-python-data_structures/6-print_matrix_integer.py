#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for i in range(len(matrix[n])):
            if i < len(matrix[n]) - 1:
                print("{:d}".format(matrix[n][i]), end=" ")
            else:
                print("{:d}".format(matrix[n][i]), end="")
        print("")
