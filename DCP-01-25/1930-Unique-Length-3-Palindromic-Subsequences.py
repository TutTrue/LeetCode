class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l = set(s[0])
        r = Counter(s)
        r[s[0]] -= 1
        res = set()

        for i in range(1, len(s) - 1):
            r[s[i]] -= 1
            for val in l:
                if r[val] > 0:
                    res.add(s[i] + val)
            l.add(s[i])

        return len(res)
