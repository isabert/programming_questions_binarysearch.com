# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def recur(root):
            if (root == None):
                return 0
            root.val = recur(root.left) + root.val + recur(root.right)
            return root.val

        recur(root);
        return root