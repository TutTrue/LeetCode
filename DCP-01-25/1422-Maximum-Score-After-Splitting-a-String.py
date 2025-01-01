class Solution:
    def maxScore(self, s: str) -> int:
        cur = s.count("1")
        cur = cur - 1 if s[0] == "1" else cur + 1
        res = cur

        for i in range(1, len(s) - 1):
            if s[i] == "0":
                cur += 1
            else:
                cur -= 1
            if cur > res:
                res = cur

        return res
