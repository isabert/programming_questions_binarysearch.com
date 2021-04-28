class Solution:
    def solve(self, nums):
        nums_sorted = []
        for e in nums:
            nums_sorted.append(e)

        nums_sorted.sort()

        res = 0
        for i in range(len(nums)):
            if (nums[i] == nums_sorted[i]):
                res += 1

        return res
