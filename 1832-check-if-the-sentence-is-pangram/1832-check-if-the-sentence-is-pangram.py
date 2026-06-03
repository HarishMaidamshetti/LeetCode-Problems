class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr=[0]*26
        for ch in sentence:
            arr[ord(ch)%97]=1
        return sum(arr)==26
        