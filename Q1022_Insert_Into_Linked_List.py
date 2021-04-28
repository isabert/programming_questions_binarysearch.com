# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, pos, val):
        new = LLNode(val)

        if pos == 0:
            new.next = head
            return new

        temp = head
        while temp and pos != 1:
            temp = temp.next
            pos -= 1
        new.next = temp.next
        temp.next = new

        return head

