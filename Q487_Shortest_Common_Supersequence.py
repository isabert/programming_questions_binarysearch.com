class Solution:
    def solve(self, a, b):
        #add " " for a and b for dp
        a = ' '+a
        b = ' '+b
        dp = [[0]*len(b) for i in range(len(a))]

        for i in range(1,len(a)):
            for j in range(1, len(b)):
                    if(a[i]==b[j]): dp[i][j]= dp[i-1][j-1]+1
                    dp[i][j] = max(dp[i][j],dp[i-1][j], dp[i][j-1])

        #-2 is to remove 2 " "
        return len(a)+len(b)-dp[len(a)-1][len(b)-1]-2