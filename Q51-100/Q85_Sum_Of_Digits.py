class Solution:
    def solve(self, num):
        res = 0
        while(num>0):
            res+=(num%10)
            num//=10

        return res