class Solution:
    def solve(self, blocks):
        dp = {}
        blocks.sort()
        for bl in blocks:
            if (dp.get(bl[0]) == None):
                dp[bl[0]] = 0
            if (dp.get(bl[1]) == None):
                dp[bl[1]] = 0
            dp[bl[1]] = max(dp[bl[1]], dp[bl[0]] + 1)

        mx = 0
        for t in dp:
            if (dp[t] > mx):
                mx = dp[t]
        return mx

