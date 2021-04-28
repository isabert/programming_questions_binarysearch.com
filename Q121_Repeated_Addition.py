class Solution:
    def solve(self, n):
        while(n>=10):
            res = 0
            while(True):
                if(n==0):
                    break
                res+=n%10
                n//=10
            n = res

        return n