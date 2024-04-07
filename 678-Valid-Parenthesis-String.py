class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def rec(st=0, i=0):
            if st == -1:
                return False
            if i == len(s):
                return st == 0
            res = False
            if s[i] == '*':
                res = rec(st+1, i+1) or rec(st, i+1) or rec(st-1, i+1)
            elif s[i] == '(':
                res = rec(st+1, i+1)
            else:
                res = rec(st-1, i+1)

            return res
        return rec()