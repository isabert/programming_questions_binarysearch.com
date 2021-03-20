class Solution:
    # if we graph nums[i]'s cost(x-axis = i, y-axis = cost(i)), we will discover that it looks like an absolute value function(like parabolas)
    # if we combine all those cost function, the combination of all the cost functions will also be like a parabola(decrease, minimum, increase) if we assume the 2 arrays are sorted with key =nums[i]
    # we shall use techniques core techinque of binary search(divide range in half) to find the minimum
    #
    def solve(self, nums, costs):
        if (len(nums) == 0 or len(nums) == 1):
            return 0
        pairs = sorted(zip(nums, costs))
        l = pairs[0][0]
        r = pairs[len(pairs) - 1][0]
        m = (l + r) // 2

        def calc_cost(n):
            t = 0
            for i in range(len(nums)):
                t += abs(nums[i] - n) * costs[i]
            return t

        while (l <= r):
            print(l)
            print(r)
            if (calc_cost(m) <= calc_cost(m + 1) and calc_cost(m) <= calc_cost(m - 1)):
                return calc_cost(m)

            elif (calc_cost(m - 1) <= calc_cost(m) and calc_cost(m) <= calc_cost(m + 1)):
                r = m - 1
            else:
                l = m + 1

            m = (l + r) // 2

    def solve1(self, nums, costs):

        pairs = [(nums[i], costs[i]) for i in range(len(nums))]
        pairs.sort()
        nums = []
        costs = []
        for i in range(len(pairs)):
            n = pairs[i][0]
            c = pairs[i][1]
            if (len(nums) == 0 or nums[len(nums) - 1] != n):
                nums.append(n)
                costs.append(c)
            else:
                costs[len(costs) - 1] += c
        res = [None] * len(nums)

        if (len(nums) == 1 or len(nums) == 0):
            return 0

        # binary search
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        def calc_cost(ind):
            if (ind < 0 or ind >= len(nums)):
                return None
            if res[ind] != None:
                return res[ind]
            else:
                res[ind] = 0
                for i in range(len(nums)):
                    res[ind] += abs(nums[i] - nums[ind]) * costs[i]
                return res[ind]

        while (l <= r):
            lc = calc_cost(m - 1)
            mc = calc_cost(m)
            rc = calc_cost(m + 1)
            if (lc == None):
                if (mc < rc):
                    return mc
                else:
                    return rc
            elif (rc == None):
                if (lc < mc):
                    return lc
                else:
                    return mc
            else:
                if (lc >= mc and rc >= mc):
                    return mc
                elif (lc >= mc and mc >= rc):
                    l = m + 1
                    m = (l + r) // 2
                else:
                    r = m - 1
                    m = (l + r) // 2

            print(res)