class Solution:
    def solve(self, nums):
        n = len(nums)
        # left side of an element has to be always smaller
        # right side of an element has to be always larger


        #prefix sum
        max_from_left = [None] * n

        #suffix sum
        min_from_right = [None] * n

        for i in range(n):
            if(i==0):
                max_from_left[i] = nums[i]-1
            else:
                max_from_left[i] = max(nums[i-1],  max_from_left[i-1])

        for i in range(n-1,-1,-1):
            if(i==n-1):
                min_from_right[i] = nums[i] + 1
            else:
                min_from_right[i] = min(nums[i+1], min_from_right[i+1])

        res = 0
        for i in range(n):
            if(max_from_left[i]< nums[i] and nums[i]<min_from_right[i]):
                res+=1

        return res