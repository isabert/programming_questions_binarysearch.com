class Solution:
    def solve(self, matrix):
        if(matrix==[]): return []
        n = len(matrix)
        m = len(matrix[0])

        transpose = [[0]*n for j in range(m)]

        for i in range(n):
            for j in range(m):
                transpose[j][i] = matrix[i][j]

        return transpose