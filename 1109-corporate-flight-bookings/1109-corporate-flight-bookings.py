class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        queries=len(bookings)
        nums=[0]*n

        for i in range(queries):
            left, right , value=bookings[i]
            nums[left-1]+=value
            if right<n:
                nums[right]-=value
        for i in range(1,n):
            nums[i]+=nums[i-1]

        return nums

        