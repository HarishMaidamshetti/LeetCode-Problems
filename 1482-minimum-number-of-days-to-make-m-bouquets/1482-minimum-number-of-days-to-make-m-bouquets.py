class Solution:
    def isPossible(self, bloomDay, m, k, mid):
        count = 0
        no_of_bouquets = 0
        
        for day in bloomDay:
            if day <= mid:
                count += 1
            else:
                no_of_bouquets += (count // k)
                count = 0
                
        no_of_bouquets += (count // k)
        return no_of_bouquets >= m

    def minDays(self, bloomDay, m, k):
        val = m * k
        if val > len(bloomDay):
            return -1
            
        low = min(bloomDay)
        high = max(bloomDay)
        result = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if self.isPossible(bloomDay, m, k, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result