import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=sorted([x**2 for x in nums])
        return result
        