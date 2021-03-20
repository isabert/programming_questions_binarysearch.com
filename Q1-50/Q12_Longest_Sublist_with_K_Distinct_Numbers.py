class Solution:
    def solve(self, k, nums):
        if (k == 0): return 0
        occurance_num = {}
        max_length = 1
        distinct = 0
        head_i = 0
        tail_i = 0

        while (head_i != len(nums)):
            occurance_h = occurance_num.get(nums[head_i])
            if occurance_h == None or occurance_h == 0:
                distinct += 1
                occurance_num[nums[head_i]] = 1
            else:
                occurance_num[nums[head_i]] += 1

            if (distinct <= k):
                max_length = max(max_length, head_i - tail_i + 1)
                head_i += 1
            else:
                while (distinct > k):
                    occurance_num[nums[tail_i]] -= 1
                    if (occurance_num[nums[tail_i]] == 0):
                        distinct -= 1
                    tail_i += 1

                head_i += 1

        return max_length
