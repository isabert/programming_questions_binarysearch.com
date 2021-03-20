class Solution:
    def solve(self, s):
        chrs = [0]*26
        for c in s:
            chrs[ord(c)-ord('a')]+=1

        count_odd = 0
        for c in chrs:
            if(c%2): count_odd+=1

        if(count_odd<=1): return True;
        else: return False