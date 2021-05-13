class Solution:
    def solve(self, intervals):
        if (len(intervals) == 0):
            return None;

        common = intervals[0];

        for interval in intervals:
            if (common[0] < interval[0]):
                common[0] = interval[0]

            if (common[1] > interval[1]):
                common[1] = interval[1]

        return common