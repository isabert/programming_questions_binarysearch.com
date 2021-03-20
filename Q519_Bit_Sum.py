class Solution:
    # NO NEGATIVES
    def solve1(self, nums, k):
        exp = 2
        total = 0
        while (True):
            for i in range(len(nums)):
                if (exp == 2):
                    total += nums[i]
                if (nums[i] % 2 == 0 and k != 0):
                    total += exp // 2
                    k -= 1
                nums[i] //= 2
                if (k == 0 and exp != 2):
                    return total % 1000000007
            exp *= 2

    def solve(self, nums, k):
        # masking, this method is faster
        exp = 1
        total = 0
        for n in nums:
            total += n

        while (True):
            for n in nums:
                if (n & exp == 0 and k != 0):
                    total += exp
                    k -= 1
                if (k <= 0):
                    return total % 1000000007
            exp *= 2