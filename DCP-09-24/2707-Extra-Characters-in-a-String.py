class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dic = {}
        def rec(i):
            if i == len(s):
                return 0
            if i in dic:
                return dic[i]

            res = 1 + rec(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, rec(j+1))
            dic[i] = res
            return res
        return rec(0)