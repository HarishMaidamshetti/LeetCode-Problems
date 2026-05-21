class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums=list(map(str,nums))
        # def compare(a,b):
        #     if a+b>b+a: return -1
        #     elif a+b<b+a: return 1
        #     else: return 0
        # nums.sort(key=cmp_to_key(compare))
        # result=''.join(nums)
        # return '0' if result[0]=='0' else result  
       
#===================================>
       
        nums=list(map(str,nums))
        nums.sort(key = lambda x : x*10, reverse=True)
        res = "".join(nums)
        return '0' if res[0] == '0' else res
        
          