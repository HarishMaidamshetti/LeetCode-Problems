class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff = [0] * 101 
        for birth, death in logs:
            diff[birth - 1950] += 1
            diff[death - 1950] -= 1
        curr = 0
        max_pop = 0
        year = 1950
        for i in range(101):
            curr += diff[i]
            if curr > max_pop:
                max_pop = curr
                year = 1950 + i
        return year
        