import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        max_num = max(nums)
        n = len(nums)
        
        # dp[gcd1][gcd2] stores the count of pairs with those GCDs
        # 0 represents an empty subsequence (initial state)
        dp = {}
        dp[(0, 0)] = 1
        
        for num in nums:
            next_dp = {}
            for (g1, g2), count in dp.items():
                # Choice 1: Skip the current number
                next_dp[(g1, g2)] = (next_dp.get((g1, g2), 0) + count) % MOD
                
                # Choice 2: Add to the first subsequence
                new_g1 = math.gcd(g1, num) if g1 != 0 else num
                next_dp[(new_g1, g2)] = (next_dp.get((new_g1, g2), 0) + count) % MOD
                
                # Choice 3: Add to the second subsequence
                new_g2 = math.gcd(g2, num) if g2 != 0 else num
                next_dp[(g1, new_g2)] = (next_dp.get((g1, new_g2), 0) + count) % MOD
                
            dp = next_dp
            
        # Sum up all states where both subsequences have the same non-zero GCD
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans
