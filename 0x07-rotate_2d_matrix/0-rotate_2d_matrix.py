#!/usr/bin/python3
"""rotate an n x n 2D matrix 90 degrees clockwise'"""


def rotate_2d_matrix(matrix):
    '''rotate an n x n 2D matrix 90 degrees clockwise'''
    start = 0
    nrow = len(matrix) - 1
    while start < nrow:
        for x in range(start, nrow):
            temp = matrix[x][nrow]
            matrix[x][nrow] = matrix[start][x]
            temp1 = matrix[nrow][nrow + start - x]
            matrix[nrow][nrow + start - x] = temp
            temp = matrix[nrow + start - x][start]
            matrix[nrow + start - x][start] = temp1
            matrix[start][x] = temp
        start += 1
        nrow -= 1
