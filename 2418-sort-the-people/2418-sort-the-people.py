class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_and_hights=[]
        for i in range(len(names)):
            names_and_hights.append([names[i] ,heights[i]])
        names_and_hights.sort(key=lambda x:x[1],reverse=True)
        return ([i[0] for i in names_and_hights])
        