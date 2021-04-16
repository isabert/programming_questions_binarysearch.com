class Solution:
    def solve(self, s0, s1):
        #ok lets say s0 and s1 are rotated vrsions of each other.
        #so we have to check if s0 is present in circularly roated s1
        #basically check if s0 in s1+s1
        #there is a edge case s0 = a and s1 = aa(so we need to check the length first)
        if(len(s0)!=len(s1)):
            return False
        s1+=s1
        if(s0 in s1):
            return True
        else:
            return False