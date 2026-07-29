import collections

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = collections.Counter(s)
        half_counts = [0] * 26
        mid_char = ""
        odd_count = 0
        
        for char, freq in counts.items():
            if freq % 2 == 1:
                odd_count += 1
                mid_char = char
            half_counts[ord(char) - ord('a')] = freq // 2
            
        if odd_count > 1:
            return ""
            
        total_len = sum(half_counts)
        
        def nCk(n, r):
            if r > n or r < 0:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n - r:
                r = n - r
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= k:
                    return k
            return res

        def get_total_perms(freqs):
            total = sum(freqs)
            res = 1
            for f in freqs:
                if f > 0:
                    res *= nCk(total, f)
                    if res >= k:
                        return k
                    total -= f
            return res

        if k > get_total_perms(half_counts):
            return ""
            
        left_half = []
        
        for i in range(total_len):
            for c_idx in range(26):
                if half_counts[c_idx] == 0:
                    continue
                
                half_counts[c_idx] -= 1
                perms = get_total_perms(half_counts)
                
                if k <= perms:
                    left_half.append(chr(ord('a') + c_idx))
                    break
                else:
                    k -= perms
                    half_counts[c_idx] += 1
                    
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]
