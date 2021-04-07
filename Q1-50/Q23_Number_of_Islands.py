class Solution:
    def solve(self, matrix):
        count = 0
        n = len(matrix)
        m = len(matrix[0])

        def rec(i,j):
            if((0<=i<n and 0<=j<m)==False):
                return
            if(matrix[i][j]==0):
                return
            #matrix[i][j]==1
            matrix[i][j]=0
            rec(i-1,j)
            rec(i+1,j)
            rec(i,j-1)
            rec(i,j+1)

        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==1):
                    count+=1
                    rec(i,j)

        return count