from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If the start or end cell is blocked, no clear path exists
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
            
        # Initialize the queue with (row, col, distance)
        queue = [(0, 0, 1)]
        grid[0][0] = 1  # Mark the starting cell as visited by overwriting it to 1
        
        # 8-directional movement offsets
        directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],           [0, 1],
            [1, -1],  [1, 0],  [1, 1]
        ]
        
        while queue:
            row, col, dist = queue.pop(0)
            
            # If we reached the bottom-right cell, return the distance
            if row == n - 1 and col == n - 1:
                return dist
                
            for direction in directions:
                nr = row + direction[0]
                nc = col + direction[1]
                
                # Check grid boundaries and if the neighboring cell is clear (0)
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # Mark as visited immediately to avoid duplicate processing
                    queue.append((nr, nc, dist + 1))
                    
        return -1