class Solution:
    def solve(self, s0, s1):
        cnt_0 = [0] * 26
        cnt_1 = [0] * 26

        for c in s0:
            cnt_0[ord(c) - ord('a')] += 1

        for c in s1:
            cnt_1[ord(c) - ord('a')] += 1

        for i in range(26):
            if (cnt_0[i] != cnt_1[i]):
                return False

        return True