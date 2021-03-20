class Solution:
    def solve(self, s1, s2):
        if (s1 == ''): return True
        i_1 = 0
        for i_2 in range(len(s2)):
            if (s1[i_1] == s2[i_2]):
                i_1 += 1
            if (i_1 == len(s1)):
                return True
        return False
