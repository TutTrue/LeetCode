class Solution:
    def compressedString(self, word: str) -> str:
        res = []

        r, l = 0, 0
        c = 0
        while r < len(word):
            while r < len(word) and word[l] == word[r] and r - l < 9:
                r+=1
            res.append(str(r - l))
            res.append(word[l])
            l = r
            
        return ''.join(res)