class Solution:
    def solve(self, n):
        s = str(n)
        length = len(s)
        res = 0
        for c in s:
            res+=int(c)**length

        return res==n
