#very simillar to day_12, except X = [1,2]
#the solution needs to be modded by 10E9+7
class Solution:
    def solve(self, N):
        X = [1, 2]
        sol = [0] * (N + 1)
        sol[0] = 1
        for i in range(1, (N + 1)):
            for x in X:
                if (i - x) >= 0:
                    sol[i] = sol[i] + sol[i - x]

        # mod the result:
        return sol[N] % 1000000007
