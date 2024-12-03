class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        i = 0
        j = 0

        while i < len(s):
            if j < len(spaces) and spaces[j] == i:
                res.append(' ')
                j+=1
            res.append(s[i])
            i+=1

        return ''.join(res)