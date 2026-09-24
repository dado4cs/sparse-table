from math import log2


class MinSparseTable:
    def __init__(self, arr: list):
        self.n = len(arr)
        y = int(log2(self.n)) + 1
        self.mat = [[0 for _ in range(self.n)] for _ in range(y)]
        for i in range(0, self.n):
            self.mat[0][i] = arr[i]
        for j in range(1, y):
            rango = self.n - 2**j + 1
            for i in range(0, rango):
                off = i + 2 ** (j - 1)
                self.mat[j][i] = min(self.mat[j - 1][i], self.mat[j - 1][off])

    def min(self, left, right):
        size = right - left + 1
        y = int(log2(size))
        op1 = self.mat[y][left]
        op2 = self.mat[y][right - 2**y + 1]
        return min(op1, op2)
