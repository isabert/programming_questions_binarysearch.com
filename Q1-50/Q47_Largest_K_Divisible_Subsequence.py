class Solution:
    def solve(self, nums, k):
        mod_result = [[] for i in range(k)]
        for i in nums:
            mod_result[i % k].append(i)
        for li in mod_result:
            li.sort(reverse=True)
        total_sum = 0
        def rec(arr, total, remainder, nxt):
            if (nxt >= k):
                if (remainder == 0): return total
                return 0
            s = 0
            t = 0
            s = rec(arr, total, remainder, nxt + 1)
            for i in range(len(arr[nxt])):
                t += arr[nxt][i]
                s = max(s, rec(arr, total + t, ((i + 1) * nxt + remainder) % k, nxt + 1))

            return s

        total_sum += rec(arr=mod_result, total=0, remainder=0, nxt=0)
        return total_sum

    def solve(self, nums, k):
        # this is about continuous update of numbers
        # do not try to replace prev with i(even if you are able to bypass the problem of the initial condition). This is because largest_sum_with_remainder is continuously updated
        # initial condition's problem:
        # if reference[i]==0 does not mean largest_sum_with_remainder[(i+nums)%k]==nums
        largest_sum_with_remainder = [0 for i in range(k)]

        for num in nums:
            #create copy by value
            reference = largest_sum_with_remainder[:]
            for i in range(0,len(reference)):
                prev = reference[i]
                largest_sum_with_remainder[(prev+num)%k] = max((prev+num),largest_sum_with_remainder[(prev+num)%k])

        return largest_sum_with_remainder[0]