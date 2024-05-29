#!/usr/bin/python3
"""
This module is used to print the pascal triangle
I have used the recursive approach to solve the problem
"""

# pasc = []
#
# def pascal_triangle(n=0):
#     if n == 0:
#         return []
#     elif n == 1:
#         pasc.append([1])
#         return pasc
#     else:
#         pascal_triangle(n-1)
#         pasc.append([1])
#         for j in range(1, n-1):
#             pasc[n - 1].append(pasc[n - 2][j-1]+pasc[n - 2][j])
#         pasc[n-1].append(1)
#         return pasc


def pascal_triangle(n=0):
    """
    This function is used to generate the pascal triangle

    Args:
        @n: the number of rows to be generated
    """
    pasc = []
    for i in range(n):
        pasc.append([1])
        for j in range(1, i):
            pasc[i].append(pasc[i - 1][j - 1] + pasc[i - 1][j])
        if i != 0:
            pasc[i].append(1)
    return pasc
