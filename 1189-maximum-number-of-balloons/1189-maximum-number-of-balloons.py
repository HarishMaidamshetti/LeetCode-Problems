from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count frequencies of all characters in the string
        counts = Counter(text)
        
        # Return the minimum possible instances we can form
        return min(
            counts['b'], 
            counts['a'], 
            counts['l'] // 2, 
            counts['o'] // 2, 
            counts['n']
        )
