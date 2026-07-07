class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #when solving problems on grpahs:
        '''when you see keywords like :
            minimum time
            shortest
            fastest 
        then that means its a BFS solution'''

        m = len(grid)
        n = len(grid[0])

        queue = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])

        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        mins = 0

        while queue and fresh>0:
            size = len(queue)
            mins += 1

            for i in range(size):
                curr = queue.pop(0)
                row = curr[0]
                col = curr[1]

                for dir in directions:
                    nr = row + dir[0]
                    nc = col + dir[1]

                    if nr<0 or nr>=m or nc<0 or nc>=n:
                        continue
                    if grid[nr][nc] == 0 or grid[nr][nc]== 2 :
                        continue
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append([nr,nc])
        if fresh==0:
            return mins
        else:
            return -1