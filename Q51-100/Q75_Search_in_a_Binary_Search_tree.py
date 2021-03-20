# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val):
        cur = root
        while (cur != None):
            if (val == cur.val): return True
            if (val < cur.val):
                cur = cur.left
            else:
                cur = cur.right

        return False
