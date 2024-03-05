class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while r > l and s[l] == s[r]:
            c = s[l]
            while r >= l and s[l] == c:
                l+=1
            while r >= l and s[r] == c:
                r-=1
        return (r - l) + 1
        