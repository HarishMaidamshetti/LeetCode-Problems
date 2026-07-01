class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        res=high
        while low<=high:
            mid=low+(high-low)//2
            if self.isPossible(weights,days,mid):
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result
    def isPossible(self,weights,days, mid):
        count=1
        sum=0

        for i in range(len(weights)):
            sum+=weights[i]
            if sum>mid:
                count+=1
                sum=weights[i]
        return count<=days
        