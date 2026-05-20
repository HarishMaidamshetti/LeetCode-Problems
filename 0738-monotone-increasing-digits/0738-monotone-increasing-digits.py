class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        dig=list(str(n))
        point=len(dig)

        for i in range(len(dig)-1,0,-1):
            if dig[i] < dig[i-1]:
                dig[i-1]=str(int(dig[i-1])-1)
                point=i
        for i in range(point,len(dig)):
            dig[i]='9'
        return int("".join(dig))
        