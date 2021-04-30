class Solution:
    def solve(self, nums):
        if(nums==[]):
            return []

        res = []
        prev = nums[0]-1
        for n in nums:
            if(n==prev):
                res[len(res)-1].append(n)
            else:
                prev = n
                res.append([n])

        return res