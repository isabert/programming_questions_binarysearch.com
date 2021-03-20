#this question is a slight modification of day_7
class Solution:
    def solve(self, s):
        def convert_str_to_arr(s):
            s = '0'+s
            arr = []
            for i in range(len(s)):
                arr.append(int(s[i]))
            return arr;

        arr = convert_str_to_arr(s)
        m = [0]*len(arr)

        for i in range(0,len(arr)):
            if(i==0):
                m[i] = 1
            else:
                if(i-1)>=0 and arr[i]!=0:
                    m[i]+=m[i-1]
                if(i-2)>=0 and arr[i-1]!=0 and (arr[i-1]*10+arr[i])<=26:
                    m[i]+=m[i-2]

        return m[len(arr)-1]
