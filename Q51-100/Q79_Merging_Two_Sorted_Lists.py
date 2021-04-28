class Solution:
    def solve(self, a, b):
        #merge sort
        res = []
        i =0
        j = 0
        while(len(res)<(len(a)+len(b))):
            if(i==len(a)):
                res.append(b[j])
                j+=1
            elif(j==len(b)):
                res.append(a[i])
                i+=1
            else:
                if(a[i]<b[j]):
                    res.append(a[i])
                    i+=1
                else:
                    res.append(b[j]);
                    j+=1

        return res