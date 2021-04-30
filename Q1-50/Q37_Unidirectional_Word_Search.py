class Solution:
    def solve(self, board, word):
        l = len(word)
        n = len(board)
        m = len(board[0]) if n>1 else 0
        dic = []
        if(n==0 or m==0):
            return False

        #horizontal words:
        if(m>=l):
            for i in range(n):
                w = ""
                for j in range(m):
                    w+=board[i][j]
                dic.append(w)

        if(n>=l):
            for j in range(m):
                w = ""
                for i in range(n):
                    w = w+board[i][j]
                dic.append(w)

        for w in dic:
            if(word in w):
                return True
        return False