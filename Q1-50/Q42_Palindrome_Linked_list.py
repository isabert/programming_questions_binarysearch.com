# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self,node):
        pass
        # from putao: Find the middle node, then reverse the right part, loop the left and the right part meanwhile to check it.

    def solve_alt(self, node):
        arr = []
        while (node != None):
            arr.append(node.val)
            node = node.next

        n = len(arr)
        for i in range(n):
            if (arr[i] != arr[n - 1 - i]):
                return False

        return True