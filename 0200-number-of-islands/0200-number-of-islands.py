class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid) # Removed 'visited'
                    count += 1
                    
        return count
    
    def dfs(self, row, col, grid): # Removed 'visited'
        m = len(grid)
        n = len(grid[0])
        
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        if grid[row][col] == '0':
            return
            
        grid[row][col] = '0' # Fixed typo from == to =
        
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row + 1, col, grid)
        self.dfs(row, col - 1, grid)