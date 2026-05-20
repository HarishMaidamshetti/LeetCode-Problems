class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # n=len(points)
        # points.sort(key=lambda x: x[1])

        # end=points[0][1]
        # arr=0
        # left=0

        # while left<n:
        #     end=points[left][1]
        #     right=left+1

        #     while right<n and points[right][0]<=end:
        #         right+=1
        #     arr+=1
        #     left=right
        
        # return arr
        
        #========================================>

        points.sort(key=lambda x:x[0])
        arr=1
        end=points[0][1]

        for i in points[1:]:
            if i[0]>end:
                arr+=1
                end=i[1]
            else:
                end=min(end,i[1])
        return arr