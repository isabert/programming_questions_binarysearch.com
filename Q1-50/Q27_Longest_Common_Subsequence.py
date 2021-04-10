class Solution:
    def solve(self, a, b):
        n = len(a)
        m = len(b)
        if(n==0 or m==0):
            return 0
        dp = [[0]*m for i in range(n)]

        dp[0][0] = 1 if(a[0]==b[0]) else 0

        for i in range(1,n):
            if(a[i]==b[0]):
                dp[i][0]=1
            else:
                dp[i][0] = dp[i-1][0]

        for j in range(1,m):
            if(a[0]==b[j]):
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1,n):
            for j in range(1,m):
                if(a[i]==b[j]):
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n-1][m-1]