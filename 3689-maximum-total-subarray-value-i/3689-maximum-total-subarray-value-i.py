class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        global_max = max(nums)
        global_min = min(nums)
        
        
        return (global_max - global_min) * k

        