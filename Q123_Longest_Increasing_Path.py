class Solution:
    def solve1(self, matrix):
        # this is the recursion version
        # dp is for the increasing path length at i,j
        # dp[i][j]=None mean didn't visit
        # lip is the longest increasing path
        n = len(matrix)
        m = len(matrix[0])

        lip = 1
        dp = [[None] * m for i in range(n)]

        def rec(i, j):
            if (dp[i][j] != None):
                return dp[i][j]
            dp[i][j] = 1

            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (in_range(ii, jj) == False):
                    continue
                if (matrix[ii][jj] > matrix[i][j]):
                    rec(ii, jj)
                    dp[i][j] = max(dp[i][j], dp[ii][jj] + 1)

            return dp[i][j]

        def in_range(i, j):
            if (i < 0 or i >= n or j < 0 or j >= m):
                return False
            return True

        def is_smaller(i, j):
            if (in_range(i - 1, j) and matrix[i][j] < matrix[i - 1][j]):
                return True
            if (in_range(i + 1, j) and matrix[i][j] < matrix[i + 1][j]):
                return True
            if (in_range(i, j - 1) and matrix[i][j] < matrix[i][j - 1]):
                return True
            if (in_range(i, j + 1) and matrix[i][j] < matrix[i][j + 1]):
                return True
            return False

        for i in range(n):
            for j in range(m):
                if (is_smaller(i, j)):
                    lip = max(lip, rec(i, j))

        return lip
    def solve2(self, A):
        # storing the length and width of the matrix for convenience
        N, M = len(A), len(A[0])
        # a helper function to return all the indices of all the neighbouring cells to a given valid index
        def neighbours(i, j):
            res = []
            # check whether an element is present below the current cell
            if i + 1 < N:
                res.append((i + 1, j))
            # check whether an element is present above the current cell
            if i - 1 >= 0:
                res.append((i - 1, j))
            # check whether an element is present to the right of current cell
            if j + 1 < M:
                res.append((i, j + 1))
            # check whether an element is present to the right of current cell
            if j - 1 >= 0:
                res.append((i, j - 1))
            return res

        dp = []
        # intializing the all the elements in the dp to -1
        for i in range(N):
            var = []
            for j in range(M):
                var.append(-1)
            dp.append(var)
        # storing the element present in index i,j
        indices = {(i, j): A[i][j] for i in range(N) for j in range(M)}
        # iterate through all the index starting from the index containing the largest element to the index containing the smallest element
        for index, val in sorted(indices.items(), reverse=True, key=lambda elem: elem[1]):
            i, j = index
            # set the current length of the largest path starting from this index to 1
            dp[i][j] = 1
            # iterate through all the neighbouring index
            for x, y in neighbours(i, j):
                # check whether the neighbour's value is strictly greater than the current index's value
                if A[x][y] > val:
                    # set dp[i][j] to the max of the current value or the neighbouring value +1
                    dp[i][j] = max(dp[i][j], 1 + dp[x][y])
        # return the largest path in dp
        return max([max(dp[i]) for i in range(N)])