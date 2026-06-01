class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        j=0
        total=0
        cost.sort(reverse=True)
        for i in cost:
            if j==2:
                j=0
                continue
            total+=i
            j+=1
        return total




            


        
        