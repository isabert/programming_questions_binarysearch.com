class Solution:
    def solve(self, n):
        fib_prev  =1
        fib_cur  = 1
        if(n==1 or n==2): return 1
        for i in range(2, n):
            t  = fib_cur+fib_prev
            fib_prev, fib_cur = fib_cur, t
        return fib_cur