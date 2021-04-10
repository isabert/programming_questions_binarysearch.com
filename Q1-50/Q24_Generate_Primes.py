class Solution:
    def solve(self, n):
        if(n==0 or n==1):
            return []
        arr = [i+1 for i in range(n)]
        arr[1-1] = 0
        for i in range(2,n+1):
            if(arr[i-1]==0):
                continue
            j = i
            while(j+i-1<n):
                j+=i
                arr[j-1]=0

        res = []
        for i in arr:
            if(i!=0):
                res.append(i)

        return res