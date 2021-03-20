class Solution:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for i in range(n)]
        if matrix[0][0]==0:
            dp[0][0]=1

        for i in range(n):
            for j in range(m):
                if(i==0 and j==0): continue
                if(matrix[i][j]==1): continue
                if(j==0):
                    dp[i][0] = dp[i-1][0]
                elif(i==0):
                    dp[0][j]= dp[0][j-1]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[n-1][m-1]%1000000007
