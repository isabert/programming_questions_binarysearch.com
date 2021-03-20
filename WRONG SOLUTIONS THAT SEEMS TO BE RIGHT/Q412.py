class Solution:
    def solve(self, nums, target):
        #2 pointers method, this is a WRONG METHOD
        #worst time: O(N^2)
        #actually wrong for this test case:
        #nums = [1, 1, 999, -1, 1000]
        #target = 1998

        head = 0
        tail = 0
        total = 0
        final_length = -1
        length = 0
        if(nums==[]):
            return -1
        if(target==0):
            for n in nums:
                if n>=0:
                    return 1
            return -1
        while(head<len(nums)):
            if(nums[head]<0):
                head +=1
                tail +=1
                length=0
                total=0
                continue
            if(total<target):
                total+=nums[head]
                head+=1
                length+=1
            while(total>=target):
                if(final_length==-1 or length<final_length):
                    final_length=length
                total-=nums[tail]
                tail+=1
                length-=1
        return final_length