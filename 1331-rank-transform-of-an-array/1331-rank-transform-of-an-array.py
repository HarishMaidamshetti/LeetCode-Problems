class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Remove duplicates and sort to establish unique ranks
        rank_map = {val: rank for rank, val in enumerate(sorted(set(arr)), 1)}
        
        # Map original elements to their calculated ranks
        return [rank_map[num] for num in arr]
