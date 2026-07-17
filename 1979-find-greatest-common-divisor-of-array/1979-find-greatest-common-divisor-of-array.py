class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[0]
        b=nums[-1]
        while b!=0:
            a,b=b, a%b
        return a
        