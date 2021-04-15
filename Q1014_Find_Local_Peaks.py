class Solution:
    def solve(self, nums):
        res  =[]
        if(len(nums)==1):
            return []
        for i in range(len(nums)):
            if(i==0 and nums[i]>nums[i+1]):
                res.append(i)
            elif(i==len(nums)-1 and nums[i]>nums[i-1]):
                res.append(i)
            elif(i!=0 and i!=len(nums)-1 and nums[i-1]<nums[i] and nums[i]>nums[i+1]):
                res.append(i)

        return res