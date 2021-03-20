class Solution:
    def solve(self, nums):
        max_step = nums[0]
        for i in range(len(nums)):
            if(max_step<i): return False;
            max_step = max(max_step,nums[i]+i)

        return True




solution = Solution()
nums = [2,4,0,1,0]
print(solution.solve(nums))