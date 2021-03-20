# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        slow = node
        fast = node
        while (fast.next != None):
            fast = fast.next
            slow = slow.next
            if (fast.next != None):
                fast = fast.next

        return slow.val
