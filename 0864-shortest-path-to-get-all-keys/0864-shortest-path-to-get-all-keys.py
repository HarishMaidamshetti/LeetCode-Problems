class Solution:
    def shortestPathAllKeys(self, grid):

        m = len(grid)
        n = len(grid[0])

        k = 0
        startRow = 0
        startCol = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    startRow = i
                    startCol = j
                elif grid[i][j] >= 'a' and grid[i][j] <= 'f':
                    k += 1

        visited = [[[False] * (1 << k) for i in range(n)] for i in range(m)]
        visited[startRow][startCol][0] = True

        queue = []
        queue.append([startRow, startCol, 0, 0])

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        while queue:
            row, col, steps, state = queue.pop(0)

            if state == (1 << k) - 1:
                return steps
            
            for dir in directions:
                nr = row + dir[0]
                nc = col + dir[1]
            
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                
                if grid[nr][nc] == '#':
                    continue
                
                if grid[nr][nc] >= 'A' and grid[nr][nc] <= 'F':
                    if state & (1 << (ord(grid[nr][nc]) - ord('A'))) == 0:
                        continue
                
                newState = state
                
                if grid[nr][nc] >= 'a' and grid[nr][nc] <= 'f':
                    newState |= (1 << (ord(grid[nr][nc]) - ord('a')))
                
                if visited[nr][nc][newState]:
                    continue
                
                visited[nr][nc][newState] = True
                queue.append([nr, nc, steps + 1, newState])
            
        return -1        