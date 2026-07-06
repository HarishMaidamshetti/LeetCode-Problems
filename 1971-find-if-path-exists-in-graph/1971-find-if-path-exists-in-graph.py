class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = [[] for i in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = [False] * n
        # Fixed typo: changed self.dbs to self.dfs
        return self.dfs(source, visited, adjList, destination) 
        
    def dfs(self, node, visited, adjList, destination):
        if node == destination:
            return True
        visited[node] = True
        for neighbour in adjList[node]:
            if not visited[neighbour]:
                if self.dfs(neighbour, visited, adjList, destination):
                    return True
        return False
