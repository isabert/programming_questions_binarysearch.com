class Solution:
    def solve(self, nums, target):
        # time constraint: O(logn)
        # this can be done with normal searching, but binary searching saves time

        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = (l + r) // 2
            if (nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target)):
                return mid + 1
            elif (nums[mid] <= target):
                l = mid + 1

            else:
                r = mid - 1

        return l