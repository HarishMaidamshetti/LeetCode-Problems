class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        la=[0]
        ra=[]
        for i in range(1,len(nums)+1):
            ra.append(sum(nums[i:]))
            la.append(sum(nums[:i]))
        ra.append(0)
        for i in range(len(nums)):
            nums[i]=abs(la[i]-ra[i])
        return nums
        