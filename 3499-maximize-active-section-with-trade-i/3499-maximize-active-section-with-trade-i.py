class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        base_ones = s.count('1')
        zero_blocks = []
        current_zeros = 0
        
        for char in s:
            if char == '0':
                current_zeros += 1
            else:
                if current_zeros > 0:
                    zero_blocks.append(current_zeros)
                    current_zeros = 0
        if current_zeros > 0:
            zero_blocks.append(current_zeros)
            
        if len(zero_blocks) < 2:
            return base_ones
            
        max_gain = 0
        for i in range(len(zero_blocks) - 1):
            gain = zero_blocks[i] + zero_blocks[i+1]
            max_gain = max(max_gain, gain)
            
        return base_ones + max_gain
