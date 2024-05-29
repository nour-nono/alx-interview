#!/usr/bin/python3
"""
This module is used to print the pascal triangle
I have used the recursive approach to solve the problem
and wrote the code for the iterative approach as well but commented it
"""
# def pascal_triangle(n):
#     pasc = []
#     for i in range(n):
#         pasc.append([])
#         pasc[i].append(1)
#         for j in range(1, i):
#             pasc[i].append(pasc[i - 1][j - 1] + pasc[i - 1][j])
#         if n != 0:
#             pasc[i].append(1)
#     for i in range(n):
#         print("[", end="")
#         for j in range(0, i):
#             print(pasc[i][j], end=",")
#         print(pasc[i][i], end="]")
#         print()
#     return pasc


pasc = []


def pascal_triangle(n=0):
    if n == 0:
        return pasc
    elif n == 1:
        pasc.append([1])
        return pasc
    else:
        pascal_triangle(n-1)
        pasc.append([1])
        for j in range(1, n-1):
            pasc[n - 1].append(pasc[n - 2][j-1]+pasc[n - 2][j])
        pasc[n-1].append(1)
        return pasc
