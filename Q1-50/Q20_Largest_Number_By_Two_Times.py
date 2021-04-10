class Solution:
    def solve(self, nums):
        nums.sort()
        return nums[len(nums)-1]>(2*nums[len(nums)-2])