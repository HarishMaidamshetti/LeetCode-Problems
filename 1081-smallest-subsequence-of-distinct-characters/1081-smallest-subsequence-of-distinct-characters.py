class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st = []
        seen = set()
        #dic = {}
        # for i in range(len(s)):
        #     dic[s[i]] = i
        # print(dic)
        for i in range(len(s)):
            while st and st[-1] > s[i] and (st[-1] in s[i+1:]) and s[i] not in seen:
                val = st.pop()
                seen.remove(val)
            if s[i] not in seen:
                st.append(s[i])
                seen.add(s[i])
        return ''.join(st)
        