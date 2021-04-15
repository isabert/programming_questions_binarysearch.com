class Solution:
    def solve(self, n):
        res = []
        for i in range(n):
            i = i+1
            if( i%3==0 and i%5==0):
                res.append("FizzBuzz")
            elif(i%3==0):
                res.append("Fizz")
            elif(i%5==0):
                res.append("Buzz")
            else:
                res.append(str(i))

        return res