#!/usr/bin/python3
"""Doc"""


def pascal_triangle(n):
    """doc"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [[1]]
    new_add = [1, 1]
    triangle.append(new_add)

    for lvl in range(2, n):
        copy = list(triangle[lvl - 1])
        copy2 = list(triangle[lvl - 1])
        for i in range(len(copy) - 1):
            sum = copy2[i] + copy2[i + 1]
            if copy[i + 1]:
                copy[i+1] = sum
                if not copy[-1] == 1:
                    copy.append(1)
            else:
                copy.insert(i + 1, sum)
        triangle.append(copy)
    return triangle
