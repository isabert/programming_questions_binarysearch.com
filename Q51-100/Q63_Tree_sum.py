# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if(root==None): return 0
        queue = [root]
        s = 0
        while(len(queue)!=0):
            e = queue.pop(0)
            s+=e.val
            if(e.left!=None):
                queue.append(e.left)
            if(e.right!=None):
                queue.append(e.right)

        return s