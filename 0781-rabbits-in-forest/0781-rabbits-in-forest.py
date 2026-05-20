class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # answers.sort()
        # i = 0
        # j = 0
        # count = 0
        # while i < (len(answers)):
        #     if answers[i] == 0:
        #         count += 1
        #         i+=1
        #     elif i < (len(answers)) and (i+1)<len(answers):
        #         if answers[i] == answers[i+1]:
        #             i+=1
        #         else:
        #             count+= answers[i]+1
        #             i+=1
            
            

        # return count
        
        #==================================>
        freq=Counter(answers)
        total=0
        for i, count in freq.items():
            gs=i+1
            groups=(count+gs-1)//gs
            total+=groups*gs
        return total
        