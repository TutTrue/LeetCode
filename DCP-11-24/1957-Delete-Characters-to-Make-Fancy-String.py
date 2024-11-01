class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for c in s:
            res.append(c)
            if len(res) > 2 and res[-1] == res[-2] == res[-3]:
                res.pop()
        return ''.join(res)