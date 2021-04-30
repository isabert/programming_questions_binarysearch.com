class Solution:
    def solve(self, nums):
        n = len(nums)
        if (n <= 2):
            return n

        dp = [[2] * n for i in range(n)]
        res = 2
        self.indices = {}
        for i in range(n):
            if (self.indices.get(nums[i]) == None):
                self.indices[nums[i]] = []
            self.indices[nums[i]].append(i)

        for i in range(n):
            for j in range(n):
                if (i < j):
                    dif = nums[j] - nums[i]
                    nxt = nums[i] - dif
                    try:
                        #### find the last index before i-1
                        ind = self.find_max_ind(val=nxt, mx=i - 1)
                        ###################################
                        if (ind == -1):
                            raise ValueError
                        dp[i][j] = max(dp[i][j], dp[ind][i] + 1)
                        res = max(dp[i][j], res)
                    except ValueError:
                        pass
        return res

    def find_max_ind(self, val, mx):
        if (self.indices.get(val) == None):
            return -1
        arr = self.indices[val]
        l = 0
        r = len(arr) - 1
        while (l <= r):
            mid = (l + r) // 2
            if (arr[mid] == mx):
                return mx
            elif (arr[mid] < mx):
                l = l + 1

            elif (arr[mid] > mx):
                r = r - 1

        return arr[l - 1] if l > 0 else -1
