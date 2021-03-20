class Solution:
    def solve(self, n):
        sol = []
        def check_three(i):
            s = str(i);
            for c in s:
                if(c=='3' or c=='6' or c=='9'):
                    return True
            return False
        for i in range(1,n+1):
            if(i%3==0 or check_three(i)==True):
                sol.append('clap')
            else:
                sol.append(str(i))

        return sol