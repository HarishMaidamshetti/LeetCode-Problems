class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp=sorted(nums)
        left=len(nums)
        right=0

        for i in range(len(nums)):
            if temp[i] != nums[i]:
                right=max(i,right)
                left=min(i,left)
        if right-left <0: return 0
        return right-left+1
        