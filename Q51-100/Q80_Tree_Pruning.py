# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def rec(root):
            if (root == None):
                return True
            if (root.left == None and root.right == None):
                return True if root.val == 0 else False

            rl = rec(root.left)
            rr = rec(root.right)

            if (rl == True):
                root.left = None
            if (rr == True):
                root.right = None

            if (rl == True and rr == True and root.val == 0):
                return True

            return False

        if (rec(root)):
            return None
        else:
            return root