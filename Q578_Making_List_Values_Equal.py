class Solution:
    def solve(self, nums):
        maxn = nums[0]
        minn = nums[0]

        for n in nums:
            if(n>maxn):
                maxn = n

            if(n<minn):
                minn = n

        return maxn-minn