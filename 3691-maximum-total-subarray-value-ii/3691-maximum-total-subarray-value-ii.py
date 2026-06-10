
import math

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0
            
        # 1. Build Sparse Table for O(1) Range Max & Min Queries
        max_log = int(math.log2(n)) + 1
        st_max = [[0] * max_log for _ in range(n)]
        st_min = [[0] * max_log for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, max_log):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                
        def query_val(L, R):
            if L > R:
                return 0
            length = R - L + 1
            j = int(math.log2(length))
            mx = max(st_max[L][j], st_max[R - (1 << j) + 1][j])
            mn = min(st_min[L][j], st_min[R - (1 << j) + 1][j])
            return mx - mn

        # 2. Initialize Max-Heap with maximum possible spans for each starting index
        # Python's heapq is a min-heap, so we invert values to track the maximums
        heap = []
        for l in range(n):
            val = query_val(l, n - 1)
            # Structure: (-value, l, r)
            heapq.heappush(heap, (-val, l, n - 1))
            
        total_value = 0
        
        # 3. Extract the top K elements
        for _ in range(k):
            if not heap:
                break
                
            neg_val, l, r = heapq.heappop(heap)
            total_value += (-neg_val)
            
            # If the subarray can be shrunk further from the right, push the next candidate
            if r > l:
                next_r = r - 1
                next_val = query_val(l, next_r)
                heapq.heappush(heap, (-next_val, l, next_r))
                
        return total_value

        