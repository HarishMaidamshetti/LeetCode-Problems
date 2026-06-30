class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        result=[0]* n
        for i in range(n-1,-1,-1):
            if nums[left]>nums[right]:
                result[i]=nums[left]**2
                left+=1
            else:
                result[i]=nums[right]**2
                right-=1
        return sorted(result)