class Solution:
    def solve(self, nums0, nums1, dist, cost):
        # @jzzhao's insight: l0==l1
        l0 = len(nums0)
        dp0 = [None] * l0

        l1 = len(nums1)
        dp1 = [None] * l1

        if (l0 == 0 or l1 == 0):
            return 0

        dp0[0] = nums0[0]
        dp1[0] = nums1[0]
        for i in range(max(l0, l1)):
            n0_avail = i < l0
            n1_avail = i < l1
            for d in range(1, dist + 1):
                if (i + d < l0):
                    if (dp0[i + d] == None):
                        dp0[i + d] = min(dp0[i] + nums0[i + d], dp1[i] + nums0[i + d] + cost)
                    else:
                        dp0[i + d] = min(min(dp0[i] + nums0[i + d], dp1[i] + nums0[i + d] + cost), dp0[i + d])

                    if (dp1[i + d] == None):
                        dp1[i + d] = min(dp1[i] + nums1[i + d], dp0[i] + nums1[i + d] + cost)
                    else:
                        dp1[i + d] = min(min(dp1[i] + nums1[i + d], dp0[i] + nums1[i + d] + cost), dp1[i + d])

        return min(dp0[l0 - 1], dp1[l1 - 1])