from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Initialize search space using the correct input variable name
        low = max(nums)
        high = sum(nums)
        result = high
        
        # Binary search for the minimum largest subarray sum
        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossible(nums, k, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        
    def isPossible(self, nums: List[int], k: int, mid: int) -> bool:
        count = 1
        current_sum = 0
        
        for weight in nums:
            # If a single element exceeds mid, this mid capacity is impossible
            if weight > mid:
                return False
                
            current_sum += weight
            if current_sum > mid:
                count += 1
                current_sum = weight
                
        return count <= k
