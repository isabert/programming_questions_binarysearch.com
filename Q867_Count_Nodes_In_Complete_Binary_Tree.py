# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # this mean's a node's child is either 0 or 2
        if (root == None):
            return 0

        t = root
        queue = []

        queue.append(t)
        counter = 1
        while (len(queue)):
            t = queue[0]
            queue.pop(0)
            if (t.left != None):
                queue.append(t.left)
                counter += 1
            if (t.right != None):
                queue.append(t.right)
                counter += 1

        return counter