# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        res = 0
        while(node!=None):
            res*=2
            res+=node.val
            node = node.next
        return res