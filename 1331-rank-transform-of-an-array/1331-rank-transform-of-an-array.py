import heapq

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if not arr:
            return []
            
        # Create a min-heap with (value, original_index) tuples
        heap = [(num, i) for i, num in enumerate(arr)]
        heapq.heapify(heap)
        
        # Result array to populate by original index
        ranks = [0] * len(arr)
        
        current_rank = 0
        last_val = float('-inf')
        
        # Process elements from smallest to largest
        while heap:
            val, idx = heapq.heappop(heap)
            
            # Increment rank only if we encounter a strictly larger value
            if val > last_val:
                current_rank += 1
                last_val = val
                
            ranks[idx] = current_rank
            
        return ranks
