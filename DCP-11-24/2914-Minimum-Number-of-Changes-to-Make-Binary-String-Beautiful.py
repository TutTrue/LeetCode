class Solution:
    def minChanges(self, s: str) -> int:
        l, r = 0, 1
        res = 0
        while r < len(s):
            if s[l] != s[r]:
                res+=1
            l+=2
            r+=2
        return res
