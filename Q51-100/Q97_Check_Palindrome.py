class Solution:
    def solve(self, s):
        half = len(s)//2

        for i in range(half):
            if(s[i]!=s[len(s)-1-i]):
                return False

        return True