class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = []
        for i in s:
            st.append(i)
        for j in t:
            if j in st:
                st.remove(j)
            else:
                return False
        return st == []
        