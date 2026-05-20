class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smin=arrays[0][0]
        smax=arrays[0][-1]

        dif=0

        for i in range(1,len(arrays)):
            curmin=arrays[i][0]
            curmax=arrays[i][-1]

            dif= max(dif,curmax-smin)
            dif=max(dif, smax-curmin)

            smin=min(smin, curmin)
            smax=max(smax,curmax)

        return dif
        