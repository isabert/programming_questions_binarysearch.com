class Solution:

    def solve(self, nums, k):
        count = {}
        for i in nums:
            if(count.get(i)==None):
                count[i]=1
            else:count[i]+=1

        for num in count:
            if(count.get(k-num)!=None):
                if(k-num)!=num or count[k-num]>1:
                    return True
        return False
s = Solution()
nums = [35, 8, 18, 3, 22,6]
k = 12
print(s.solve(nums,k))