#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []

    if (n <= 0):
        return triangle

    for row in range(n):
        oldtriangle = triangle.copy()
        for pos in range(len(triangle)):
            if pos > 0:
                triangle[pos] = oldtriangle[pos] + oldtriangle[pos - 1]
        triangle.append(1)
        display = ','.join(map(str, triangle))
        print(f'[{display}]')
