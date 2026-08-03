class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        two_steps_back = 1
        one_step_back = 2
        
        for _ in range(3, n + 1):
            current_steps = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = current_steps
            
        return one_step_back
