class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cover= set()
        for i, j in nums:
            for s in range(i, j + 1):
                cover.add(s)
        return len(cover)
        