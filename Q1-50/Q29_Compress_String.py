class Solution:
    def solve(self, s):
        res  =""
        for c in s:
            if(len(res)==0):
                res = res+c
            if(res[len(res)-1]!=c):
                res = res+c

        return res