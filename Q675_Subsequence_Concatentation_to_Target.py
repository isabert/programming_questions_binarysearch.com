#need a hint?
#https://dmoj.ca/problem/ac20p3
class Solution:
    def solve(self, s, t):
        has_new = False
        count = -1
        t_ind = 0
        if(len(t)==0): return 0
        while(True):
            has_new=False
            for i in range(len(s)):
                if(t_ind==len(t)):break
                if(s[i]==t[t_ind]):
                    t_ind+=1
                    has_new=True

            if(has_new==True):
                if(count==-1): count=0
                count+=1
            if(has_new==False):return count