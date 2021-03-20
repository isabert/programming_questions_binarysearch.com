class Solution:
    def solve(self, n, k):
        total_combo = 1
        for i in range(1, n + 1):
            total_combo *= i

        nums = [i for i in range(1, n + 1)]

        st = ""

        while (len(nums)):
            t = k // (total_combo // len(nums))
            k = k % (total_combo // len(nums))
            total_combo //= len(nums)
            val = nums.pop(t)
            st += str(val)

        return st