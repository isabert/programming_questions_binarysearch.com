class Solution:
    def solve1(self, nums):
        # the dp method
        # time:O(n^2)
        # space:O(n)
        dp = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i + 1):
                if (nums[i] <= nums[j]):
                    continue
                else:
                    # increasing
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp) if dp != [] else 0

    def solve(self, nums):
        # the binary search method
        # time :O(n*logn)
        # space O(n)
        #this method uses binary search to find the location to insert the value N
        pseudo_lis = []

        def binary_search(num):
            l = 0
            r = len(pseudo_lis) - 1
            m = (l + r) // 2
            while (l <= r):
                if (num == pseudo_lis[m]):
                    return m
                elif (num < pseudo_lis[m]):
                    r = m - 1
                    m = (l + r) // 2
                else:
                    l = m + 1
                    m = (l + r) // 2
            return l

        for n in nums:
            i = binary_search(n)
            if (i == len(pseudo_lis)):
                pseudo_lis.append(n)
            else:
                pseudo_lis[i] = n

        return len(pseudo_lis)