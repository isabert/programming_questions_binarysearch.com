class Solution:
    def solve(self, rooms, target):
        for r in rooms:
            if(r>=target):
                return r
        return -1