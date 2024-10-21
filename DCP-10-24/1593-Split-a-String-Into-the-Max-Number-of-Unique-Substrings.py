class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        found = set()
        m = 0

        def backtrack(i):
            nonlocal m
            if i == len(s):
                m = max(m, len(found))
                return
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                if tmp not in found:
                    found.add(tmp)
                    backtrack(j+1)
                    found.remove(tmp)
        backtrack(0)
        return m