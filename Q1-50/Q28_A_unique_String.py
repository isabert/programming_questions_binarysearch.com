class Solution:
    def solve1(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        for e in count:
            if (e > 1): return False

        return True

    def solve(self, s):
        # we can use bit operations to make this work too
        count = 0
        for c in s:
            res = 1 << (ord(c) - ord('a'))
            if (res & count == 0):
                count |= 1 << (ord(c) - ord('a'))
            else:
                return False

        return True