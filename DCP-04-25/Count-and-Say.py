class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        if n == 2: return '11'
        if n == 3: return '21'
        x = self.countAndSay(n-1)
        res = ''
        l = 0
        while l < len(x):
            r = l
            while r < len(x) and x[r] == x[l]:
                r+=1
            res += f'{(r - l)}{x[l]}'
            l = r
        return res