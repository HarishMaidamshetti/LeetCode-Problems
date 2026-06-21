class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # Step 1: Add boundary restrictions
        restrictions.append([1, 0])
        restrictions.sort()
        
        # If the last building is not in restrictions, add its theoretical max boundary
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
            
        m = len(restrictions)
        
        # Step 2: Left-to-Right Scan
        for i in range(1, m):
            idx1, h1 = restrictions[i-1]
            idx2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (idx2 - idx1))
            
        # Step 3: Right-to-Left Scan
        for i in range(m - 2, -1, -1):
            idx1, h1 = restrictions[i]
            idx2, h2 = restrictions[i+1]
            restrictions[i][1] = min(h1, h2 + (idx2 - idx1))
            
        # Step 4: Find the absolute maximum peak height
        max_height = 0
        for i in range(m - 1):
            idx1, h1 = restrictions[i]
            idx2, h2 = restrictions[i+1]
            # Calculate the peak height between two adjacent restricted buildings
            peak = (h1 + h2 + (idx2 - idx1)) // 2
            max_height = max(max_height, peak)
            
        return max_height
