# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if (root == None): return True
        return self.rec(root, root.val)

    def rec(self, root, val):
        if (root.left == None and root.right == None): return root.val == val
        res = (root.val == val)
        if (root.left != None):
            res = res and self.rec(root.left, val)

        if (root.right != None):
            res = res and self.rec(root.right, val)

        return res