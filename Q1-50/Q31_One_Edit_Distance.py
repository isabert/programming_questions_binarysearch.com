class Solution:
    def solve(self, s0, s1):
        n = len(s0)
        m = len(s1)
        if(m==0 and n==0):
            return True

        if(m==0 and n==1):
            return True

        if(n==0 and m==1):
            return True

        if(abs(m-n)>1):
            return False

        if(m==n):
            # replace
            dif = 0
            for i in range(m):
                if(s0[i]!=s1[i]):
                    dif+=1
                if(dif>1):
                    return False
            return True
        else:
            # add or delete
            short_s = s1
            long_s = s0
            if(m>n):
                long_s = s1
                short_s = s0
            skip = 0
            i_s = 0
            for i_l in range(len(long_s)):
                if i_s==len(short_s):
                    skip+=1
                elif(long_s[i_l]==short_s[i_s]):
                    i_s+=1
                else:
                    skip+=1
                if(skip>1):
                    return False
            return True
