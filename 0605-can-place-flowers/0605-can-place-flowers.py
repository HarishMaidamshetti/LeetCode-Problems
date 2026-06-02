class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        size = len(fb)
        i = 0
        while( i < size and n > 0 ):
            if( fb[i] == 1): 
                i += 2 
            elif( i - 1 == -1 and i + 1 < size and fb[i] == 0 and fb[i + 1] == 0 ):
                n -= 1 
                i += 2
            elif( fb[i - 1] == 0 and fb[i] == 0 and i == size - 1):
                n -= 1
                i += 2
            elif( i + 1 < size and i - 1 >= 0 and fb[i - 1] == 0 and  fb[i] == 0 and (i + 1 == size or fb[i + 1] == 0)):
                n -= 1 
                i += 2
            else:
                i += 1

        return  False if n > 0 else True 
        