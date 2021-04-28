class Solution:
    def solve(self, s):
        res = 0
        temp = 0
        for c in s:
            if(ord(c)-ord("0")>=0 and ord(c)-ord("0")<=9):
                res-=temp
                temp=temp*10+ord(c)-ord("0")
                res+=temp
            else:
                temp=0
        return res