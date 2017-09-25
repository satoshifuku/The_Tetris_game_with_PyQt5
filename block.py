# -*- config: utf-8 -*-

import sys
import numpy as np


class Block(object):
    def __init__(self):
        self.list = []
        block_o = np.array([[0, 0, 0, 0],
                            [0, 1, 1, 0],
                            [0, 1, 1, 0],
                            [0, 0, 0, 0]])
        self.list.append(block_o)

        block_z = np.array([[0, 0, 0, 0],
                            [2, 2, 0, 0],
                            [0, 2, 2, 0],
                            [0, 0, 0, 0]])
        block_s = np.array([[0, 0, 0, 0],
                            [0, 3, 3, 0],
                            [3, 3, 0, 0],
                            [0, 0, 0, 0]])
        self.list.append(block_z)
        self.list.append(block_s)

        block_j = np.array([[0, 0, 0, 0],
                            [4, 4, 4, 0],
                            [0, 0, 4, 0],
                            [0, 0, 0, 0]])
        block_l = np.array([[0, 0, 0, 0],
                            [0, 5, 5, 5],
                            [0, 5, 0, 0],
                            [0, 0, 0, 0]])
        self.list.append(block_j)
        self.list.append(block_l)

        block_t = np.array([[0, 0, 0, 0],
                            [6, 6, 6, 0],
                            [0, 6, 0, 0],
                            [0, 0, 0, 0]])
        self.list.append(block_t)

        block_i = np.array([[0, 0, 0, 0],
                            [7, 7, 7, 7],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]])
        self.list.append(block_i)

    def rotation(self, mat):
        tmp = np.identity(4)
        for row in range(4):
            for col in range(4):
                # clockwise
                tmp[col][row] = mat[3-row][col]
                    # anticlockwise
                    # tmp[col][row] = mat[row][3-col]
        return tmp


def main():

    bl = Block()
    mat = np.copy(bl.list[4])
    for count in range(3):
        mat = np.copy(bl.rotation(mat))
    print(mat)


if __name__ == '__main__':

    main()
