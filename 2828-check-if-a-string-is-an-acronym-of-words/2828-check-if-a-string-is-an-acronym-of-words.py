class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        result=""
        for word in words:
            result+=(word[0])
        print(result)
        print("".join(word[0] for word in words))
        return ("".join(word[0] for word in words))==s
        