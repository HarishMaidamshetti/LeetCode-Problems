class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for i in s:
            if i.isnumeric():
                st.pop()
            else:
                st.append(i)
        return "".join(st)