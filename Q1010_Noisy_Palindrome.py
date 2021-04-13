class Solution:
    def solve(self, s):
        s_clean  =""
        for c in s:
            enc = ord(c)-ord("a")
            if(0<=enc<26):
                s_clean+=c

        for i in range(len(s_clean)//2):
            if(s_clean[i]!=s_clean[len(s_clean)-1-i]):
                return False
        return True