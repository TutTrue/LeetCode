class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = [''] * len(s)
        i = 0
        idx = 0
        cnt = 0
        while i < len(s):
            if s[i] == '(':
                cnt+=1
                res[idx] = s[i]
                idx += 1
            elif s[i] == ')' and cnt > 0:
                res[idx] = s[i]
                idx+= 1
                cnt-=1
            elif s[i] != ')':
                res[idx] = s[i]
                idx+=1
            i += 1
        while cnt > 0:
            if res[idx - 1] == '(':
                res[idx - 1] = ''
                cnt-=1
            idx -= 1
        return ''.join(res)        