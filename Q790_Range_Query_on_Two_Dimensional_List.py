class RangeSumMatrix:
    def __init__(self, matrix):
        self.res = []
        self.n = len(matrix)
        self.m = len(matrix[0])

        self.res = [[0] * self.m for i in range(self.n)]

        for i0 in range(self.n):
            for j0 in range(self.m):
                # res holds the sum from matrix[i0][j0] to matrix[n][m]
                i = self.n - 1 - i0
                j = self.m - 1 - j0
                self.res[i][j] = matrix[i][j]
                if (i == self.n - 1 and j == self.m - 1): continue
                if (i != self.n - 1):
                    self.res[i][j] += self.res[i + 1][j]
                if (j != self.m - 1):
                    self.res[i][j] += self.res[i][j + 1]
                if (i != self.n - 1 and j != self.m - 1):
                    self.res[i][j] -= self.res[i + 1][j + 1]

        return None

    def total(self, row0, col0, row1, col1):
        s = self.res[row0][col0]
        if (col1 != self.m - 1):
            s -= self.res[row0][col1 + 1]

        if (row1 != self.n - 1):
            s -= self.res[row1 + 1][col0]

        if (col1 != self.m - 1 and row1 != self.n - 1):
            s += self.res[row1 + 1][col1 + 1]
        return s