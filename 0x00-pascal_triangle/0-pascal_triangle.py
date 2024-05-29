#!/usr/bin/python3
"""
This module is used to print the pascal triangle
I have used the recursive approach to solve the problem
"""


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
