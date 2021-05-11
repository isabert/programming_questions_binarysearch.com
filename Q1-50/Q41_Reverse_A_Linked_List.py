# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        cur = head
        head = None;
        while (cur != None):
            t = cur.next;
            cur.next = head;
            head = cur;
            cur = t;

        return head;

    def solve_slow(self, node):
        if(node==None):
            return None
        stack = []
        t = node
        while(t!=None):
            stack.append(t)
            t = t.next

        for i in range(len(stack)):
            if(i!=0):
                stack[i].next = stack[i-1]
            else:
                stack[i].next = None

        return stack[len(stack)-1]