class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        s.sort(key=lambda x:x[-1])
        result=""
        for i in s:
            result+=" "+i[:-1]
        return result.strip()

        