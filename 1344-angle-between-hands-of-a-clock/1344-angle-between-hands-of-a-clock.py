class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6.0
        hour_angle = (hour % 12) * 30.0 + minutes * 0.5
        
        # Find the absolute difference
        diff = abs(hour_angle - minute_angle)
        
        # Return the smaller angle
        return min(diff, 360.0 - diff)
        