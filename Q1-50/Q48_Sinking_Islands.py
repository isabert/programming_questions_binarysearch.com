class Solution:
    def solve(self, board):
        n = len(board)
        m = len(board[0])
        res = [[0] * m for i in range(n)]

        def dfs(x, y):
            if (x < 0 or x >= n): return
            if (y < 0 or y >= m): return
            if (board[x][y] == 0): return
            if (res[x][y] == 1): return
            res[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        # just check the boarders
        for i in range(n):
            if (res[i][0] == 0 and board[i][0] == 1):
                dfs(i, 0)
            if (res[i][m - 1] == 0 and board[i][m - 1] == 1):
                dfs(i, m - 1)
        for j in range(m):
            if (res[0][j] == 0 and board[0][j] == 1):
                dfs(0, j)
            if (res[n - 1][j] == 0 and board[n - 1][j] == 1):
                dfs(n - 1, j)

        return res