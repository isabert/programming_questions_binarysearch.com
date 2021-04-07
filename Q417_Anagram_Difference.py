from functools import lru_cache
class Solution:
    def swap(self, s, i, j):
        ret = ""
        ret += s[0:i]
        ret += s[j]
        ret += s[i+1 : j]
        ret += s[i]
        ret += s[j + 1 : len(s)]
        return ret
    def solve(self, s0, s1):
        #Q: how do you know if it's a backtracking problem?
        #A(@wyzwyzlo): you can tell that a problem is backtracking if the constraints are super low
        #like less than 30
        #and if it requires like testing all combinations
        #if the constraints are super low then its either:
        #1.brute force
        #2.backtracking
        #3.bitset DP
        @lru_cache(None)
        def rec(s0,s1,ind,count):
            if(ind>=len(s0)):
                    return count
            if(s0[ind]==s1[ind]):
                return rec(s0,s1,ind+1,count)
            min_res = None
            for i in range(ind+1, len(s0)):
                if(s1[ind]==s0[i]):
                    s0 = self.swap(s0,ind,i)
                    r = rec(s0,s1,ind+1,count+1)
                    if(min_res==None or r<min_res):
                        min_res = r
                    s0 = self.swap(s0,ind,i)
            return min_res

        return rec(s0,s1,0,0)
