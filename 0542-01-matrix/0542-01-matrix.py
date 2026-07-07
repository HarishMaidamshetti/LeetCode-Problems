class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        queue = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i,j])
                else:
                    mat[i][j] = -1

        directions = [[-1,0], [0,-1], [1,0], [0,1]]

        while queue:
            size = len(queue)

            for i in range(size):
                curr = queue.pop(0)
                row = curr[0]
                col = curr[1]

                for dir in directions:
                    nr = row + dir[0]
                    nc = col + dir[1]

                    if nr<0 or nr>=m or nc<0 or nc>=n:
                        continue
                    if mat[nr][nc]!= -1 :
                        continue
                    
                    mat[nr][nc] = mat[row][col] + 1
                    queue.append([nr,nc])
        return mat