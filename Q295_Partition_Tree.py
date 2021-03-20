# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        queue = [root]
        leaves = 0
        nodes = 0
        while(len(queue)):
            element = queue.pop(len(queue)-1)
            if(element==None): continue
            queue.append(element.left)
            queue.append(element.right)

            if(element.left==None and element.right==None):
                leaves+=1
            else:
                nodes+=1
        return [leaves,nodes]