class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'[^a-zA-Z0-9]', '', s)
        st = st.lower()
        l, r = 0, len(st) - 1
        while r > l:
            if st[r] != st[l]:
                return False
            r-=1
            l+=1
        return True
