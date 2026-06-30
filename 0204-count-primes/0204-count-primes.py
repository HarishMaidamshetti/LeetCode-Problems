from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        primes=[True]*(n+1)
        primes[0]=primes[1]=False

        for i in range(2, int(sqrt(n))+1):
            if primes[i]:
                for j in range(i*i, n+1,i):
                    primes[j]=False
        
        count=0
        for i in range(2,n):
            if primes[i]:
                count+=1
        return count
        