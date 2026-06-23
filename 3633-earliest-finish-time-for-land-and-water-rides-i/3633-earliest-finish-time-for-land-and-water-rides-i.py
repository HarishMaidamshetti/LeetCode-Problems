from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def calc(a1, t1, a2, t2):
            mn = min(a + b for a, b in zip(a1, t1))
            return min(max(mn, a) + b for a, b in zip(a2, t2))

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )