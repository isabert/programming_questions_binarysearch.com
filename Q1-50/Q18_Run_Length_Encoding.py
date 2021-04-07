class Solution:
    def solve(self, s):
        counter = 0
        character  =s[0]
        sol = ""
        for c in s:
            if(c !=character):
                sol = sol+str(counter)+character
                counter = 0
                character = c
            counter+=1
        sol = sol+str(counter)+character

        return sol
