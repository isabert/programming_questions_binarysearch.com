class Solution:
    def solve(self, nums):
        count = {}
        for num in nums:
            if(count.get(num)==None):
                count[num]=1
            else:
                count[num]+=1

        occurance = {}
        for key,val in count.items():
            if(occurance.get(val)==None):
                occurance[val]=True
            else:
                return False
        print(occurance)
        return True