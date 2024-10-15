class Solution:
    def minimumSteps(self, s: str) -> int:
        pos = 0
        res = 0
        for i, c in enumerate(s):
            if c == '0':
                res += (i - pos)
                pos+=1
        return res