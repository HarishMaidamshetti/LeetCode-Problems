class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        total_count = 0
        
        for num in nums:
            # Handle special edge case if target digit is 0
            if num == 0 and digit == 0:
                total_count += 1
                continue
                
            # Extract digits mathematically
            while num > 0:
                if num % 10 == digit:
                    total_count += 1
                num //= 10
                
        return total_count
