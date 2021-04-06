class Solution:
    def solve(self, nums):
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        res = 0
        for i in range(0, len(nums), 1):
            if (i == 0):
                left_max[i] = nums[i]
            else:
                left_max[i] = max(left_max[i - 1], nums[i])

        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1):
                right_max[i] = nums[i]
            else:
                right_max[i] = max(nums[i], right_max[i + 1])

        for i in range(0, len(nums)):
            h = min(left_max[i], right_max[i])
            if (h > nums[i]):
                res += h - nums[i]

        return res