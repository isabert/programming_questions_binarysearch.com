# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        res = end = node
        count = 0
        while(end.next!=None):
            end = end.next
            count+=1
            if(count>k):
                res = res.next
        return res.val

    def solve_alt(self, node, k):
        if (node == None):
            return None

        last_ind = 0
        t = node
        while (t.next != None):
            t = t.next
            last_ind += 1

        ind = last_ind - k
        i = 0
        t = node
        while (i < ind):
            i += 1
            t = t.next

        return t.val
