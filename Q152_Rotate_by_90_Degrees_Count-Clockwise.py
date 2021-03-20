class Solution:
    #m is the rotation of matrix
    #one of the solution is from the matrix's perspective
    #the other is from m's perspective
    def solve1(self, matrix):
        m = [[0] * len(matrix) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                m[row][col] = matrix[col][len(matrix) - 1 - row]

        return m

    def solve2(self, matrix):
        m = [[0] * len(matrix) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                m[len(matrix) - 1 - col][row] = matrix[row][col]

        return m
