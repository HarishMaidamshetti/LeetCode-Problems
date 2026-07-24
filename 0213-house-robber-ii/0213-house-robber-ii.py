class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(arr):
            prev1, prev2 = 0, 0
            for money in arr:
                new_max = max(prev1 + money, prev2)
                prev1 = prev2
                prev2 = new_max
            return prev2

        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])

        return max(case1, case2)