from collections import deque
import math

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        MOD = 1_000_000_007
        n = len(edges) + 1
        
        # 1. Build adjacency list (1-indexed nodes)
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 2. Determine binary lifting table size
        LOG = math.ceil(math.log2(n)) + 1
        up = [[-1] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        # 3. Iterative BFS to establish tree structure (prevents recursion limits)
        queue = deque([1])
        visited = {1}
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth[neighbor] = depth[curr] + 1
                    up[0][neighbor] = curr
                    queue.append(neighbor)
                    
        # 4. Fill the binary lifting sparse table
        for i in range(1, LOG):
            for node in range(1, n + 1):
                if up[i - 1][node] != -1:
                    up[i][node] = up[i - 1][up[i - 1][node]]
                    
        # Helper function to find LCA via binary lifting
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u  # Keep u deeper than v
                
            # Bring u to the same depth level as v
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[i][u]
                    
            if u == v:
                return u
                
            # Lift both nodes simultaneously right beneath their LCA
            for i in range(LOG - 1, -1, -1):
                if up[i][u] != up[i][v]:
                    u = up[i][u]
                    v = up[i][v]
                    
            return up[0][u]

        # 5. Process queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)  # Path of length 0 cannot have an odd sum
            else:
                lca_node = get_lca(u, v)
                # Compute path distance (number of edges)
                path_length = depth[u] + depth[v] - 2 * depth[lca_node]
                # Formula: 2^(path_length - 1) % MOD
                ans.append(pow(2, path_length - 1, MOD))
                
        return ans
