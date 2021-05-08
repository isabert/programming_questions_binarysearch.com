class Solution:
    def solve(self, matrix):
        n = len(matrix)
        if(n==0):
            return -1
        m = len(matrix[0])
        if(m==0):
            return -1

        for j in range(m):
            for i in range(n):
                if(matrix[i][j]==1):
                    return j

        return -1