class Solution:
    def solve_method1(self, nums):
        #dic stores {sum:(count, last_number)}
        #time complexity: O(n^3) worst case
        dic = {}
        longest = 2
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i>j):
                    if(dic.get(nums[i]+nums[j])==None):
                        dic[nums[i]+nums[j]]=(2,[nums[i]])
                    else:
                        tup_list = dic[nums[i]+nums[j]][1]
                        tup_list.append(nums[i])
                        dic[nums[i]+nums[j]]=(2,tup_list)
        for n in nums:
            if(dic.get(n) is not None):
                longest = max(longest, dic[n][0]+1)
                cur = n
                for last in dic[n][1]:
                    l = dic[n][0]+1
                    if(dic.get(last+cur)!=None and dic.get(last+cur)[0]>=l):
                        if(dic.get(last+cur)[0]>l):
                            pass
                        if(dic.get(last+cur)[0]==l):
                            tup = dic[last+cur]
                            tup_len = tup[0]
                            tup_list = tup[1]
                            tup_list.append(cur)
                            tup_list.sort()
                            print(cur)
                            print(last+cur)
                            print(tup_list)
                            dic[last+cur] = (tup_len, tup_list)
                    else:
                        dic[last+cur] = (l, [cur])
        return longest if longest >2 else 0

    def solve(self, nums):
        n = len(nums)
        dp = [[2] * n for i in range(n)]
        maximum = 2
        for i in range(n):
            for j in range(n):
                if (i < j):
                    try:
                        ind = nums.index(nums[j] - nums[i])
                    except ValueError:
                        ind = -1
                    if (ind >= 0 and ind < i):
                        dp[i][j] = max(dp[i][j], dp[ind][i] + 1)
                        maximum = max(maximum, dp[i][j])

        # maximum = max(max(arr) for arr in dp)
        return (maximum > 2) * maximum