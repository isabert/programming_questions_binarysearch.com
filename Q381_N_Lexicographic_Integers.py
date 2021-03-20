class Solution:
    def solve_3(self,n):
        cur = 1
        sol=[]
        sol.append(cur)
        while(len(sol)<n):
            cur*=10
            while(cur>n):
                cur//=10
                cur+=1
                #also, edge case is such that we have 19 + 1 = 20 => (20/10) 2. we check this by %10.
                #this edge case will propagate imagine n=3012
                while(cur%10==0):
                    cur//=10
            sol.append(cur)

        return sol

    def solve2(self, n):
        exp = 1
        stack = []
        sol = []
        while (exp <= n):
            sol.append(exp)
            exp *= 10
        if (exp > n): exp //= 10
        cur = exp
        while (True):
            if (cur >= n):
                mod = cur % 10
                if (cur == mod): return sol
                cur //= 10
            cur += 1
            # if there are n numbers in stack, there are n trailing zeros for exp
            while (cur % 10 == 0):
                if (cur == exp): return sol
                cur //= 10
                stack.append(cur)
            while (len(stack) > 0):
                t = stack.pop(len(stack) - 1)
                sol.append(t)
                cur *= 10

            sol.append(cur)
        return sol

    def solve1(self, n):
        cnt = 1
        ans = [cnt]
        while len(ans) < n:
            cnt *= 10
            while cnt > n:
                cnt = cnt // 10
                cnt += 1
                while cnt % 10 == 0:
                    cnt = cnt // 10
            ans.append(cnt)

        return ans

