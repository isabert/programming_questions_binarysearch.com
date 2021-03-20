class Solution:
    def solve(self, integer):
        cur_n = 0
        max_n = 0

        while (integer != 0):
            cur = integer % 2
            integer //= 2
            if (cur == 0):
                cur_n = 0
            if (cur == 1):
                cur_n += 1
                max_n = max(cur_n, max_n)

        return max_n