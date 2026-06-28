class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        # Sort to arrange elements in increasing order
        arr.sort()
        
        # The first element must always be 1
        arr[0] = 1
        
        # Iterate and ensure consecutive difference is at most 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
            
        # The last element is the maximum possible value
        return arr[-1]
