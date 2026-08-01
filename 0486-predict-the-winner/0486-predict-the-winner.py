class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = list(nums)
        for d in range(1, n):
            for j in range(n - 1, d - 1, -1):
                i = j - d
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[n - 1] >= 0
