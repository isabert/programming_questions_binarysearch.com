class Solution:
    def solve(self, a, b):
        max_ind = max(len(a), len(b))+1
        res = ""
        i = 0
        carry = 0
        for i in range(max_ind):
            i_a = len(a)-i-1
            i_b = len(b)-i-1
            va = 0
            vb = 0
            if(i_a>=0 and a[i_a]=="1"):
                va = 1
            if(i_b>=0 and b[i_b]=="1"):
                vb = 1
            sum_digit = va+vb+carry
            if(i==max_ind-1):
                if(carry==1):
                    res = "1"+res
                return res
            if(sum_digit%2==1):
                res = "1"+res
            else:
                res = "0"+res
            if(sum_digit>=2):
                carry = 1
            else:
                carry = 0



