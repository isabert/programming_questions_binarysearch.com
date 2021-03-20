# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, head):
        if (head == None):
            is_uni = True
            uval = None
            num = 0
            return is_uni, uval, num
        if (head.left == None and head.right == None):
            is_uni = True
            uval = head.val
            num = 1
            return is_uni, uval, num

        l_is_uni, l_uval, l_num = self.rec(head.left)
        r_is_uni, r_uval, r_num = self.rec(head.right)

        is_uni = False
        uval = None
        num = l_num + r_num
        if (l_is_uni == True and r_is_uni == True and l_uval == r_uval and l_uval == head.val):
            is_uni = True

        if (l_is_uni == True and r_is_uni == True and (
                l_uval == None and head.val == r_uval or r_uval == None and head.val == l_uval)):
            is_uni = True

        if (is_uni == True and l_uval == r_uval):
            uval = l_uval
            num += 1

        if (is_uni == True and l_uval == None and r_uval != None):
            uval = r_uval
            num += 1

        if (is_uni == True and r_uval == None and l_uval != None):
            uval = l_uval
            num += 1
        return is_uni, uval, num

    def solve(self, root):
        is_uni, uval, num = self.rec(root)
        return num