class Solution:
    def solve(self, nums):
        dp = [[0]*len(nums) for i in range(len(nums))]
        def rec(left_boundary, right_boundary):
            if(right_boundary-left_boundary<=1):
                return 0
            select_max = 0
            select_ind = 0
            if(dp[left_boundary][right_boundary]!=0): return dp[left_boundary][right_boundary]
            for i in range(left_boundary+1, right_boundary):
                t = rec(left_boundary,i)+rec(i,right_boundary)+nums[i]
                if(select_ind==0 or t>select_max):
                    select_ind =i
                    select_max =t
            dp[left_boundary][right_boundary] =  select_max+nums[left_boundary]+nums[right_boundary]
            return dp[left_boundary][right_boundary]

        return rec(0, len(nums)-1)