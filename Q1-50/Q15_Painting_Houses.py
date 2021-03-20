class Solution:
    def solve(self, matrix):
        #to improve for O(1) space, only store 2 best colors
        n = len(matrix)
        k = len(matrix[0])
        dp= [0]*k
        dp_prev = [matrix[0][j] for j in range(k)]
        def find_min(avoid):
            min_val = None
            min_ind = None
            for i in range(len(dp_prev)):
                if(i!=avoid and (min_ind==None or dp_prev[i]<min_val)):
                    min_val = dp_prev[i]
                    min_ind = i

            return min_val, min_ind

        for i in range(1,n):
            min_val, min_ind = find_min(-1)
            for j in range(k):
                if(j!=min_ind):
                    dp[j] = min_val+matrix[i][j]
                else:
                    alt_min_val,alt_mind_ind = find_min(j)
                    dp[j]=alt_min_val+matrix[i][j]
            dp_prev = dp
            dp = [0]*k
        return min(dp_prev)