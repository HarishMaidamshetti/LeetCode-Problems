class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        dict1={0:1}
        count=0
        for ele in nums:
            sum+=ele
            count += dict1.get(sum-k,0)
            dict1[sum]=dict1.get(sum,0)+1
        return count

        