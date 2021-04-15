class Solution:
    # wrong interpretation of question: I thought the question means: how many overlapping intervals is there at interval

    # def solve(self, intervals, point):
    #     res = 0
    #     lb = point
    #     rb = point
    #     for element in intervals:
    #         if(
    #         element[0]<=lb and element[1]>=lb
    #         or element[1]>=rb and element[0]<=rb
    #         or element[0]>=lb and element[1]<=rb):
    #             res+=1
    #             lb = min(element[0], lb)
    #             rb =max(element[1], rb)

    #     return res
    def solve(self, intervals, point):
        res = 0
        for element in intervals:
            if (element[0] <= point and element[1] >= point):
                res += 1

        return res
