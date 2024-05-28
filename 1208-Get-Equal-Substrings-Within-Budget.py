class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost, l, m = 0, 0, 0
        for r in range(len(s)):
            cost+=abs(ord(s[r]) - ord(t[r]))
            while cost > maxCost:
                cost-=abs(ord(s[l]) - ord(t[l]))
                l+=1
            m = max(m, r - l + 1)
        return m