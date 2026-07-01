class Solution:
    def firstOccurence(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        result = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                result = mid
                high = mid - 1  # Look left for earlier occurrences
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return result

    def lastOccurence(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        result = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                result = mid
                low = mid + 1   # Look right for later occurrences
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return result

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.firstOccurence(nums, target)
        last = self.lastOccurence(nums, target)
        return [first, last]
