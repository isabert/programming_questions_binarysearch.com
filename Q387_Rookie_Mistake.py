class Solution:
    def solve(self, s):
        ind = 0
        for i in range(len(s)):
            if(s[i]=="R"):
                ind=i
                break

        l = True
        r = True
        for i in range(ind):
            if(s[i]=='B'):
                l=False
                break

        for i in range(ind+1, len(s)):
            if(s[i]=="B"):
                r = False
                break

        return l or r