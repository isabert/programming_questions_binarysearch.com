class Solution:
    def solve(self, nums):
        # k is the number of unique elements
        dic = {}
        for n in nums:
            if (dic.get(n) is None):
                dic[n] = 1

        return len(dic)