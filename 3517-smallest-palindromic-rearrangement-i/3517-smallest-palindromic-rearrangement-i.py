class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        
        sorted_half = "".join(sorted(s[:n // 2]))
        
        
        mid = s[n // 2] if n % 2 != 0 else ""
        
        
        return sorted_half + mid + sorted_half[::-1]
