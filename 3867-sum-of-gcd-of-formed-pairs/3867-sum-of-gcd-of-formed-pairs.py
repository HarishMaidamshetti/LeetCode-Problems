import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        current_max = 0
        
        # Step 1: Construct prefixGcd
        for num in nums:
            current_max = max(current_max, num)
            prefix_gcd.append(math.gcd(num, current_max))
            
        # Step 2: Sort
        prefix_gcd.sort()
        
        # Step 3: Two-pointer simulation
        total_sum = 0
        left, right = 0, n - 1
        while left < right:
            total_sum += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return total_sum
