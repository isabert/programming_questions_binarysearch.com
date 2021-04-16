class Solution:
    def solve(self, nums):
        res = 0
        for n in nums:
            n = str(n)
            if(len(n)%2):
                res+=1

        return res