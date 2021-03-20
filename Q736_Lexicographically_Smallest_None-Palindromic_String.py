class Solution:
    def solve(self, s):
        for i in range(len(s)):
            c = s[i]
            if c!='a' and (len(s)%2==0 or len(s)%2==1 and i!=len(s)//2):
                s = s[:i]+'a'+s[i+1:]
                return s
        s = s[:len(s)-1]+'b'
        return s