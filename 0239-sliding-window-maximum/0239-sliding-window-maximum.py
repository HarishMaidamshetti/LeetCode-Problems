from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        
        queue = deque()
        left = 0
        
        for right in range(n):
            while len(queue) > 0 and nums[right] > queue[-1]:
                queue.pop()
            queue.append(nums[right])
            
            if right - left + 1 == k:
                result.append(queue[0])
                
                if nums[left] == queue[0]:
                    queue.popleft()
                    
                left += 1
                
        return result