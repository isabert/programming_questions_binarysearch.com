class Solution:
    def solve(self, s):
        front_bracket = 0
        for c in s:
            if(c=="("): front_bracket +=1
            elif(c==")"):
                front_bracket-=1
                if(front_bracket<0): return False

        if(front_bracket>0): return False
        return True

solution = Solution()
s1 = "()"
s2 = "()()"
s3 = ")("
s4 = ""
s5 = "((()))"
s6 = "((()"
print(solution.solve(s1)==True)
print(solution.solve(s2)==True)
print(solution.solve(s3)==False)
print(solution.solve(s4)==True)
print(solution.solve(s5)==True)
print(solution.solve(s6)==False)