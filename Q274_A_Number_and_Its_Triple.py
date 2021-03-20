class Solution:
    def solve(self, nums):
        seen = set()
        for x in nums:
            if 3 * x in seen or x % 3 == 0 and x // 3 in seen:
                return True
            seen.add(x)
        return False