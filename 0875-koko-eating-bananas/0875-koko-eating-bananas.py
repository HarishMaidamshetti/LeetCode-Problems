class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        result=high
        while low<=high:
            mid=low+(high-low)//2
            if self.isPossible(piles,h,mid):
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result

    def isPossible(self, piles, h, mid):
        hours=0
        for ele in piles:
            hours+=(ele+mid-1)//mid
        return hours<=h
