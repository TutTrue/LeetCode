class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = []
        for i in range(len(s)):
            diff.append(abs(ord(s[i]) - ord(t[i])))
        
        s = 0
        l, r = 0, 0
        m = 0
        while r < len(diff):
            s+=diff[r]
            r+=1
            while s > maxCost:
                s-=diff[l]
                l+=1
            m = max(m, r - l)
        return m