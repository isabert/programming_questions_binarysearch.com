class Solution:
    def solve_ineffective(self, n):
        while(n>=10):
            res = 0
            while(True):
                if(n==0):
                    break
                res+=n%10
                n//=10
            n = res

        return n

    def solve(self, n):
        # see the proof folder for mathematically profe
        return n%9 if n%9!=0 else 9