class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = [ [False]*n for _ in range(m)]
        atlantic = [ [False]*n for _ in range(m)]

        for i in range(n):
            self.dfs(0, i, pacific, heights)
            self.dfs(m-1, i, atlantic, heights)
        
        for i in range(m):
            self.dfs(i, 0, pacific, heights)
            self.dfs(i, n-1, atlantic, heights)

        result = []

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result
    def dfs(self, row, col, visited, heights):
        m = len(heights)
        n = len(heights[0])

        visited[row][col] = True

        directions = [[-1,0], [0,-1], [1,0], [0,1]]

        for dirs in directions:
            nr = row + dirs[0]
            nc = col + dirs[1]

            if nr<0 or nr>=m or nc<0 or nc>=n:
                continue
                
            if visited[nr][nc]: 
                continue

            if heights[nr][nc] < heights[row][col]:
                continue

            self.dfs(nr, nc, visited, heights)