#!/usr/bin/python3
""" Simple python module contains Pascal Triangle function """


def pascal_triangle(n):
    """ Compute pascal's triangle """

    final = []
    if (n <= 0):
        return []

    triangle = []
    for row in range(n):
        oldtriangle = triangle.copy()
        for pos in range(len(triangle)):
            if pos > 0:
                triangle[pos] = oldtriangle[pos] + oldtriangle[pos - 1]
        triangle.append(1)
        final.append(triangle.copy())
    return final
