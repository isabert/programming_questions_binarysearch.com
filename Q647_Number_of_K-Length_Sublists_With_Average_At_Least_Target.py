class Solution:
    def solve(self, nums, k, target):
        sum_target = k*target
        count = 0
        sum_sublist = 0
        if(len(nums)<k):
            return 0

        for i in range(k-1,len(nums)):
            if(i==k-1):
                sum_sublist = sum(nums[0:k])
            else:
                sum_sublist = sum_sublist-nums[i-k]+nums[i]
            if(sum_sublist>=sum_target):
                count+=1

        return count