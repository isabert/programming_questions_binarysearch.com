# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        queue = [root]
        count  =0
        while(len(queue)):
            element  =queue.pop(len(queue)-1)
            if(element==None): continue
            v = element.val
            if(v<lo):
                queue.append(element.right)
            elif(v>hi):
                queue.append(element.left)
            else:
                queue.append(element.left)
                queue.append(element.right)
                count+=1
        return count