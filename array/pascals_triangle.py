"""
Pascal's Triangle:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly 
above it.
"""


def get_pascals_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

for r in get_pascals_triangle(5):
    print(r)

print(get_pascals_triangle(6))
