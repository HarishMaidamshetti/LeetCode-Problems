class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        
        # Build the tree adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # BFS to determine the maximum depth (number of edges)
        max_depth = 0
        queue = collections.deque([(1, 0)]) # (node, current_depth)
        visited = {1}
        
        while queue:
            u, d = queue.popleft()
            max_depth = max(max_depth, d)
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append((v, d + 1))
                    
        # Calculate 2^(max_depth - 1) % (10^9 + 7)
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)
