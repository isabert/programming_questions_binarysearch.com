# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        prev = None
        while(head!=None):
            if(prev == None):
                prev = head.val-1
            if(prev>=head.val):
                return False
            else:
                prev = head.val
                head = head.next

        return True