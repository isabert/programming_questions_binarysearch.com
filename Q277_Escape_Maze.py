class Solution:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        visited = [[None]*m for i in range(n)]
        bfs_queue = [(0,0,1)]#i,j,square number
        while(len(bfs_queue)):
            element = bfs_queue.pop(0)
            i = element[0]
            j = element[1]
            if(matrix[i][j]==1):
                visited[i][j]=-1
                continue
            if(visited[i][j]!=None):
                continue
            visited[i][j] = element[2]
            if(i+1<n):
                bfs_queue.append((i+1,j,element[2]+1))
            if(j+1<m):
                bfs_queue.append((i,j+1,element[2]+1))
            if(i-1>=0):
                bfs_queue.append((i-1,j,element[2]+1))
            if(j-1>=0):
                bfs_queue.append((i,j-1,element[2]+1))

        return visited[n-1][m-1] if visited[n-1][m-1]!=None else -1