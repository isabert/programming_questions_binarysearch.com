class Solution:
    def solve(self, n):
        res = 1#length of the collatz sequence
        while(True):
            if(n==1):
                return res
            res+=1
            if(n%2==0):
                n//=2
            else:
                n = 3*n+1