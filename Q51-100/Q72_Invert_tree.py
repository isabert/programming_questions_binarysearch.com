# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if(root==None): return root
        if(root.left==None and root.right==None):
           return root
        root.left, root.right = root.right, root.left
        self.solve(root.left)
        self.solve(root.right)
        return root