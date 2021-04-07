from functools import lru_cache
class Solution:
    def solve(self, s):
        if(s==""):
            return 0
        n = len(s)
        dp = [[0]*n for i in range(n)]
        for i in range(n):
             dp[i][i] = 1
        for length in range(1,n):
            for i in range(n):
                j=i+length
                if(j<n):
                    if(s[i]==s[j]):
                        dp[i][j] = max(dp[i+1][j-1]+2, dp[i+1][j], dp[i][j-1])
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]

    def solve2(self, s):
        @lru_cache(None)
        def rec(l, r):
            if l == r:
                return 1
            if l > r:
                return 0
            if s[l] == s[r]:
                return rec(l+1, r-1) + 2
            else:
                return max(rec(l+1, r), rec(l, r-1))
        return rec(0, len(s) - 1)