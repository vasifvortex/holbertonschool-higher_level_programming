#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [row[:] for row in matrix]
    for row in new:
        for i in range(len(row)):
            row[i] = row[i] * row[i]
    return new
