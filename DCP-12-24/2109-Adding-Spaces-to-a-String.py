class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = [''] * (len(s) + len(spaces))
        i = 0
        j = 0
        idx = 0

        while i < len(s):
            if j < len(spaces) and spaces[j] == i:
                res[idx] = ' '
                idx+=1
                j+=1
            res[idx] = s[i]
            idx+=1
            i+=1

        return ''.join(res)